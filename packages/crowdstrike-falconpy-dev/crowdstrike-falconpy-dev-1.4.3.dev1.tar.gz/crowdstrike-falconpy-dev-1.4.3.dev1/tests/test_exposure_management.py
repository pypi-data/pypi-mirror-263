# test_exposure_management.py
# This class tests the Exposure Management product class

# import json
# import os
# import sys

# # Authentication via the test_authorization.py
# from tests import test_authorization as Authorization
# # from tests.test_spotlight_vulnerabilities import TestSpotlight
# # from tests.test_spotlight_evaluation_logic import TestSpotlightEval
# # from tests.test_discover import TestDiscover
# # from tests.test_cspm_registration import TestCSPMRegistration

# # Import our sibling src folder into the path
# sys.path.append(os.path.abspath('src'))
# # Classes to test - manually imported from sibling folder
# from falconpy import ExposureManagement, PolicyManagement, DeploymentManagement, FalconIntelligenceSandbox

# auth = Authorization.TestAuthorization()
# config = auth.getConfigObject()



# AllowedResponses = [200, 201, 207, 400, 429]

# class TestExposureManagement():
#     def test_force_pass(self):
#         falcon = ExposureManagement(auth_object=config)
#         assert True

# class TestPolicyManagement():
#     def test_force_pass(self):
#         falcon = PolicyManagement(auth_object=config)
#         assert True

# class TestDeploymentManagement():
#     def test_force_pass(self):
#         falcon = DeploymentManagement(auth_object=config)
#         assert True

# class TestFalconIntelligenceSandbox():
#     def test_force_pass(self):
#         falcon = FalconIntelligenceSandbox(auth_object=config)
#         assert True
