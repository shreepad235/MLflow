import mlflow

def calculate_sum(x,y):
    return x+y


if __name__=='__main__':
   with mlflow.start_run():
       x,y=10,20
       z=calculate_sum(10,20)
       mlflow.log_param("x",x)
       mlflow.log_param("y",y)
       mlflow.log_metric("z",z)