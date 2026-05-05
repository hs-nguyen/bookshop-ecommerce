# Create ECS Execution Role
resource "aws_iam_role" "ecs_task_execution_role" {
  name = "fcaj-bookshop-ecs-task-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect    = "Allow"
        Principal = { Service = "ecs-tasks.amazonaws.com" }
        Action    = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "ecs_task_execution_role_policy" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_iam_policy" "ecs_task_excution_policy_cloudwatch" {
  name        = "ecs_task_excution_policy_cloudwatch"
  path        = "/"
  description = "Cloudwatch policy"

  policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "logs:CreateLogGroup",
            "Resource": "arn:aws:logs:ap-southeast-1:891377055161:log-group:/ecs/*"
        }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "ecs_task_excution_policy_cloudwatch_attachment" {
  role = aws_iam_role.ecs_task_execution_role.name
  policy_arn = aws_iam_policy.ecs_task_excution_policy_cloudwatch.arn
}

resource "aws_iam_role_policy_attachment" "ecs_task_execution_role_secrets_policy" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/SecretsManagerReadWrite"
}

data "aws_ecs_cluster" "main" {
  cluster_name = "fcaj-bookshop-cluster"
}

resource "aws_iam_role" "ecs_task_role" {
  name = "fcaj-bookshop-ecs-task-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect    = "Allow"
        Principal = { Service = "ecs-tasks.amazonaws.com" }
        Action    = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_policy" "ecs_task_role_policy" {
  name        = "ecs_task_role_policy"
  path        = "/"
  description = "Policy for ECS task role"

  policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "ecs:ExecuteCommand",
          "ecs:DescribeTasks",
        ],
        "Resource": [ data.aws_ecs_cluster.main.arn,"${data.aws_ecs_cluster.main.arn}/*"]
      }
    ]
  })
}
resource "aws_iam_role_policy_attachment" "ecs_task_role_policy_attachment" {
  role       = aws_iam_role.ecs_task_role.name
  policy_arn = aws_iam_policy.ecs_task_role_policy.arn
}