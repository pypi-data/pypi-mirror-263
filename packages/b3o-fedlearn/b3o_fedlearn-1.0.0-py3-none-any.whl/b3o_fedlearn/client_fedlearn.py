import numpy as np
import boto3
from client_repo import MODEL


class FLClient(object):
    def __init__(self, member_ID, x_train_client, y_train_client, x_test_client, y_test_client):
        self.nodeId = member_ID

        self.FLTaskName = None
        self.roundId = -1
        self.serverId = -1
        self.epochs_client = -1

        self.countTransaction = 1
        self.num_train_per_client = 0
        self.num_test_per_client = 0

        self.x_train_client, self.y_train_client, self.x_test_client, self.y_test_client = x_train_client, y_train_client, x_test_client, y_test_client
        self.num_train_per_client = self.x_train_client.shape[0]
        self.num_test_per_client = self.x_test_client.shape[0]
        print("Local datasets:")
        print("x_train =", self.x_train_client.shape)
        print("y_train =", self.y_train_client.shape)
        print("x_test =", self.x_test_client.shape)
        print("y_test =", self.y_test_client.shape)
        print()

    def receiveNotificationsFromServer(self, sqs_region, sqs_name, cross_account_sqs_role=None):
        if cross_account_sqs_role == None:
            sqs_obj = boto3.resource('sqs', region_name=sqs_region)
            sqs_queue = sqs_obj.get_queue_by_name(QueueName=sqs_name)
            sqs_msgs = sqs_queue.receive_messages(
                AttributeNames=['All'],
                MessageAttributeNames=['All'],
                VisibilityTimeout=15,
                WaitTimeSeconds=20,
                MaxNumberOfMessages=5
            )

            sqs_client = boto3.client('sqs', region_name=sqs_region)
            queue_url = sqs_client.get_queue_url(QueueName=sqs_name)['QueueUrl']
            for msg in sqs_msgs:
                sqs_client.delete_message(QueueUrl=queue_url,
                                          ReceiptHandle=msg.receipt_handle)
            return sqs_msgs

        elif cross_account_sqs_role is not None:
            client = boto3.client('sts')
            response = client.assume_role(RoleArn=cross_account_sqs_role,
                                          RoleSessionName='access-cross-account-sqs',
                                          DurationSeconds=900)

            sqs_obj = boto3.resource('sqs', region_name=sqs_region,
                                     aws_access_key_id=response['Credentials']['AccessKeyId'],
                                     aws_secret_access_key=response['Credentials']['SecretAccessKey'],
                                     aws_session_token=response['Credentials']['SessionToken'])

            sqs_queue = sqs_obj.get_queue_by_name(QueueName=sqs_name)
            sqs_msgs = sqs_queue.receive_messages(
                AttributeNames=['All'],
                MessageAttributeNames=['All'],
                VisibilityTimeout=15,
                WaitTimeSeconds=20,
                MaxNumberOfMessages=5
            )

            sqs_client = boto3.client('sqs', region_name=sqs_region,
                                      aws_access_key_id=response['Credentials']['AccessKeyId'],
                                      aws_secret_access_key=response['Credentials']['SecretAccessKey'],
                                      aws_session_token=response['Credentials']['SessionToken'])
            queue_url = sqs_client.get_queue_url(QueueName=sqs_name)['QueueUrl']
            for msg in sqs_msgs:
                sqs_client.delete_message(QueueUrl=queue_url,
                                          ReceiptHandle=msg.receipt_handle)
            return sqs_msgs

    def localTraining(self, model_params_w_file, s3_fl_model_registry, cross_account_s3_role=None):

        if (self.roundId == 0):
            print("2: Download a global model")
            mlmodel = MODEL.MLMODEL()
            model = mlmodel.getModel()
            prio_train_loss, prio_train_acc = "NA", "NA"
            prio_test_loss, prio_test_acc = "NA", "NA"
            print("prio local training: training loss: {} \t training accuracy: {}".format(prio_train_loss,
                                                                                           prio_train_acc))
            print("prio local training: testing loss: {} \t testing accuracy: {}".format(prio_test_loss, prio_test_acc))
            print()

            print("3: Local training ...")
            model.fit(self.x_train_client, self.y_train_client, epochs=self.epochs_client)
            after_train_loss, after_train_acc = model.evaluate(self.x_train_client, self.y_train_client, verbose=2)
            after_test_loss, after_test_acc = model.evaluate(self.x_test_client, self.y_test_client, verbose=2)
            print('after local training: training loss: %2.4f \t training accuracy: %2.4f' % (
            after_train_loss, after_train_acc))
            print('after local training: testing loss: %2.4f \t testing accuracy: %2.4f \n' % (
            after_test_loss, after_test_acc))

        else:
            mlmodel = MODEL.MLMODEL()
            model = mlmodel.getModel()

            print("2: Download a global model")

            s3 = None
            if cross_account_s3_role == None:
                s3 = boto3.resource('s3')
            elif cross_account_s3_role is not None:
                client = boto3.client('sts')
                response = client.assume_role(RoleArn=cross_account_s3_role,
                                              RoleSessionName='access-cross-account-s3',
                                              DurationSeconds=900)
                s3 = boto3.resource(
                    "s3",
                    aws_access_key_id=response['Credentials']['AccessKeyId'],
                    aws_secret_access_key=response['Credentials']['SecretAccessKey'],
                    aws_session_token=response['Credentials']['SessionToken']
                )

            s3.Bucket(s3_fl_model_registry).download_file(model_params_w_file, "models/" + model_params_w_file)
            weights_prio_training = np.load("models/" + model_params_w_file, allow_pickle=True)
            model.set_weights(weights_prio_training)

            prio_train_loss, prio_train_acc = model.evaluate(self.x_train_client, self.y_train_client, verbose=2)
            prio_test_loss, prio_test_acc = model.evaluate(self.x_test_client, self.y_test_client, verbose=2)
            print('prio local training: training loss: %2.4f \t training accuracy: %2.4f' % (
            prio_train_loss, prio_train_acc))
            print(
                'prio local training: testing loss: %2.4f \t testing accuracy: %2.4f' % (prio_test_loss, prio_test_acc))
            print()

            print("3: Local training ...")

            model.fit(self.x_train_client, self.y_train_client, epochs=self.epochs_client)
            after_train_loss, after_train_acc = model.evaluate(self.x_train_client, self.y_train_client, verbose=2)
            after_test_loss, after_test_acc = model.evaluate(self.x_test_client, self.y_test_client, verbose=2)
            print('after local training: training loss: %2.4f \t training accuracy: %2.4f' % (
            after_train_loss, after_train_acc))
            print('after local training: testing loss: %2.4f \t testing accuracy: %2.4f \n' % (
            after_test_loss, after_test_acc))

        savedModelFileName = 'train_weight_round_{}_client_{}.npy'.format(self.roundId, self.nodeId)
        weights = model.get_weights()
        np.save("models/" + savedModelFileName, weights)

        metricDict = {
            "Task_Name": self.FLTaskName,
            "Task_ID": str(self.nodeId).zfill(4) + str(self.countTransaction).zfill(8),
            "roundId": str(self.roundId),
            "member_ID": str(self.nodeId),
            "numSamples": str(self.num_train_per_client),
            "numClientEpochs": str(self.epochs_client),
            "trainLoss": str(after_train_loss),
            "trainAcc": str(after_train_acc),
            "testLoss": str(after_test_loss),
            "testAcc": str(after_test_acc),
            "weightsFile": savedModelFileName,
            "numClientsRequired": "NA",
            "source": "Client",
        }

        return savedModelFileName, metricDict

    def processGlobalModelInfoFromServer(self, transactions):

        tasks = set()

        for task in transactions:
            tasks.add(task["Task_Name"])

        latestTaskName = None
        if len(tasks) == 1:
            latestTaskName = tasks.pop()
        else:
            for taskName in list(tasks):
                if latestTaskName is None or latestTaskName < taskName:
                    latestTaskName = taskName

        latestRound = -1
        for transaction in transactions:
            if latestTaskName == transaction["Task_Name"] and latestRound < int(transaction["roundId"]):
                latestRound = int(transaction["roundId"])

        if self.FLTaskName == None or (self.FLTaskName <= latestTaskName and self.roundId < latestRound):
            self.FLTaskName = latestTaskName
            self.roundId = latestRound

        elif self.FLTaskName > latestTaskName:
            pass

        for transaction in transactions:
            if self.FLTaskName == transaction["Task_Name"] and self.roundId == int(transaction["roundId"]):
                metricDict = {
                    "roundId": transaction["roundId"],
                    "member_ID": transaction["member_ID"],
                    "numSamples": transaction["numSamples"],
                    "numClientEpochs": transaction["numClientEpochs"],
                    "trainAcc": float(transaction["trainAcc"]) if transaction["trainAcc"] != "NA" else "NA",
                    "testAcc": float(transaction["testAcc"]) if transaction["testAcc"] != "NA" else "NA",
                    "trainLoss": float(transaction["trainLoss"]) if transaction["trainLoss"] != "NA" else "NA",
                    "testLoss": float(transaction["testLoss"]) if transaction["testLoss"] != "NA" else "NA",
                    "weightsFile": transaction["weightsFile"],
                    "numClientsRequired": transaction["numClientsRequired"],
                    "source": transaction["source"],
                    "TaskToken": transaction["TaskToken"],
                }
                self.epochs_client = int(metricDict["numClientEpochs"])
                self.serverId = metricDict["member_ID"]
                return metricDict
        return None

    def uploadToFLServer(self, s3_fl_model_registry, savedModelFileName, dynamodb_table_model_info, metricDict,
                         cross_account_s3_role=None, cross_account_dynamodb_role=None):
        s3 = None
        dynamodb = None
        if cross_account_s3_role == None and cross_account_dynamodb_role == None:
            s3 = boto3.resource('s3')
            dynamodb = boto3.resource('dynamodb')
        elif cross_account_s3_role is not None and cross_account_dynamodb_role is not None:
            client = boto3.client('sts')
            response = client.assume_role(RoleArn=cross_account_s3_role,
                                          RoleSessionName='access-cross-account-s3',
                                          DurationSeconds=900)
            s3 = boto3.resource(
                "s3",
                aws_access_key_id=response['Credentials']['AccessKeyId'],
                aws_secret_access_key=response['Credentials']['SecretAccessKey'],
                aws_session_token=response['Credentials']['SessionToken']
            )

            dynamodb_client = boto3.client('sts')
            dynamodb_response = dynamodb_client.assume_role(RoleArn=cross_account_dynamodb_role,
                                                            RoleSessionName='access-cross-account-dynamoDB',
                                                            DurationSeconds=900)
            dynamodb = boto3.resource('dynamodb',
                                      aws_access_key_id=dynamodb_response['Credentials']['AccessKeyId'],
                                      aws_secret_access_key=dynamodb_response['Credentials']['SecretAccessKey'],
                                      aws_session_token=dynamodb_response['Credentials']['SessionToken'])

        s3.Bucket(s3_fl_model_registry).upload_file("models/" + savedModelFileName, savedModelFileName)

        task_table = dynamodb.Table(dynamodb_table_model_info)
        task_name = metricDict["Task_Name"]
        task_ID = metricDict["Task_ID"]
        task_table.put_item(Item=metricDict)

        printDiction = {
            "taskName": metricDict["Task_Name"],
            "taskId": metricDict["Task_ID"],
            "roundId": metricDict["roundId"],
            "memberId": metricDict["member_ID"],
            "numSamples": metricDict["numSamples"],
            "trainAcc": float(metricDict["trainAcc"]) if metricDict["trainAcc"] != "NA" else "NA",
            "testAcc": float(metricDict["testAcc"]) if metricDict["testAcc"] != "NA" else "NA",
            "trainLoss": float(metricDict["trainLoss"]) if metricDict["trainLoss"] != "NA" else "NA",
            "testLoss": float(metricDict["testLoss"]) if metricDict["testLoss"] != "NA" else "NA",
            "weightsFile": metricDict["weightsFile"],
            "source": metricDict["source"],
            "taskToken": metricDict["TaskToken"],
        }
        print("Upload local model information: {} \n\n".format(str(printDiction)))
        self.countTransaction = self.countTransaction + 1

    def downloadFLGlobalModel(self, s3_fl_model_registry, cross_account_s3_role=None):
        print("6: Download the FL trained global model for deployment")

        s3 = None
        if cross_account_s3_role == None:
            s3 = boto3.resource('s3')
        elif cross_account_s3_role is not None:
            client = boto3.client('sts')
            response = client.assume_role(RoleArn=cross_account_s3_role,
                                          RoleSessionName='access-cross-account-s3',
                                          DurationSeconds=900)
            s3 = boto3.resource(
                "s3",
                aws_access_key_id=response['Credentials']['AccessKeyId'],
                aws_secret_access_key=response['Credentials']['SecretAccessKey'],
                aws_session_token=response['Credentials']['SessionToken']
            )

        model_params_w_file = "train_weight_round_" + str(self.roundId - 1) + ".npy"
        print(model_params_w_file)
        s3.Bucket(s3_fl_model_registry).download_file(model_params_w_file, "models/" + model_params_w_file)
        return model_params_w_file
