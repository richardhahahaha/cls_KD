_base_ = [
    '../../mobilenet_v1/mobilenet_v1.py'
]
# model settings
find_unused_parameters=True
tf_nkd = True
distiller = dict(
    type='ClassificationDistiller',
    teacher_pretrained = 'https://download.openmmlab.com/mmclassification/v0/resnet/resnet50_8xb32_in1k_20210831-ea4938fc.pth',
    tf_nkd = tf_nkd,
    )

student_cfg = 'configs/mobilenet_v1/mobilenet_v1.py'
teacher_cfg = 'configs/resnet/resnet50_b32x8_imagenet.py'