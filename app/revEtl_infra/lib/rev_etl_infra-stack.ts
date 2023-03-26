import { Stack, StackProps } from "aws-cdk-lib";
import { Construct } from "constructs";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as apiGateway from "aws-cdk-lib/aws-apigateway";
// import * as dotenv from "dotenv";

// dotenv.config();

export class RevEtlInfraStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const apiLambda = new lambda.Function(this, "ApiFunction", {
      runtime: lambda.Runtime.PYTHON_3_9,
      code: lambda.Code.fromAsset("../app/"),
      handler: "main_api.handler",
    });

    

  }
}


// const layer = new lambda.LayerVersion(this, "BaseLayer", {
//   code: lambda.Code.fromAsset("lambda_base_layer/layer.zip"),
//   compatibleRuntimes: [lambda.Runtime.PYTHON_3_9],
// });


// export class CopykittInfraStack extends Stack {
//   constructor(scope: Construct, id: string, props?: StackProps) {
//     super(scope, id, props);

//     const layer = new lambda.LayerVersion(this, "BaseLayer", {
//       code: lambda.Code.fromAsset("lambda_base_layer/layer.zip"),
//       compatibleRuntimes: [lambda.Runtime.PYTHON_3_9],
//     });



//     const copyKittApi = new apiGateway.RestApi(this, "RestApi", {
//       restApiName: "CopyKitt Tutorial API",
//     });

//     copyKittApi.root.addProxy({
//       defaultIntegration: new apiGateway.LambdaIntegration(apiLambda),
//     });
//   }
// }
