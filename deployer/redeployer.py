import os

def redeploy_sls(memory: float):
    print("Redeploying with: ", memory)
    os.system('cd ../deployer/self-adaptive-memory-allocation && sls deploy --memory ' + str(memory))

def test():
    print("-------- hello")