from stable_baselines3 import PPO
import torch

input_model = "../logs/ppo/soccer_world-v0_45/best_model.zip"
onnx_path = "my_ppo_model.onnx"
observation_size = 10

class OnnxablePolicy(torch.nn.Module):
  def __init__(self, extractor, action_net, value_net):
      super(OnnxablePolicy, self).__init__()
      self.extractor = extractor
      self.action_net = action_net
      self.value_net = value_net

  def forward(self, observation):
      # NOTE: You may have to process (normalize) observation in the correct
      #       way before using this. See `common.preprocessing.preprocess_obs`
      action_hidden, value_hidden = self.extractor(observation)
      return self.action_net(action_hidden), self.value_net(value_hidden)

model = PPO.load(input_model)
model.policy.to("cpu")
onnxable_model = OnnxablePolicy(model.policy.mlp_extractor, model.policy.action_net, model.policy.value_net)

dummy_input = torch.randn(1, observation_size)
torch.onnx.export(onnxable_model, dummy_input, onnx_path, opset_version=9)

##### Load and test with onnx

import onnx
import onnxruntime as ort
import numpy as np

onnx_model = onnx.load(onnx_path)
onnx.checker.check_model(onnx_model)

observation = np.zeros((1, observation_size)).astype(np.float32)
ort_sess = ort.InferenceSession(onnx_path)
action, value = ort_sess.run(None, {'input.1': observation})
