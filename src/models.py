from torchvision.models import efficientnet_b0, EfficientNet_B0_Weights
from torch import nn

class CNN_Encoder(nn.Module):
    def __init__(self, class_n, rate=0.1):
        super(CNN_Encoder, self).__init__()  # 부모 클래스의 생성자 호출
        # EfficientNet B4 모델 불러오기 (이미지넷 가중치 포함)
        self.model = efficientnet_b0(weights=EfficientNet_B0_Weights.IMAGENET1K_V1)
        # 원래의 분류기를 교체 (1000개 클래스에서 class_n개 클래스로)
        num_ftrs = self.model.classifier[1].in_features  # 마지막 레이어의 입력 특성 수 가져오기

        self.model.classifier[1] = nn.Linear(num_ftrs, class_n)  # 새로운 선형 레이어로 교체
        print(self.model.classifier)

    def forward(self, x):
        output = self.model(x)  # 모델에 입력 전달
        return output
    


    

