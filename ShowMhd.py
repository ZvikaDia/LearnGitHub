import SimpleITK as sitk
import matplotlib.pylab as plt
ct_scans = sitk.GetArrayFromImage(sitk.ReadImage(r"D:\DIACARDIO\DATA\Camus\training\patient0002\patient0002_4CH_ES_gt.mhd", sitk.sitkFloat32))
plt.figure()
plt.gray()
plt.imshow(ct_scans[0])
# plt.subplots_adjust(0,0,1,1,0.01,0.01)
# for i in range(ct_scans.shape[0]):
#     plt.subplot(5,6,i+1), plt.imshow(ct_scans[i]), plt.axis('off')
#     # use plt.savefig(...) here if you want to save the images as .jpg, e.g.,
plt.savefig (r"D:\DeleteMe\20\test_gt.png")

ct_scans = sitk.GetArrayFromImage(sitk.ReadImage(r"D:\DIACARDIO\DATA\Camus\training\patient0002\patient0002_4CH_ES.mhd", sitk.sitkFloat32))
plt.figure()
plt.gray()
plt.imshow(ct_scans[0])
# plt.subplots_adjust(0,0,1,1,0.01,0.01)
# for i in range(ct_scans.shape[0]):
#     plt.subplot(5,6,i+1), plt.imshow(ct_scans[i]), plt.axis('off')
#     # use plt.savefig(...) here if you want to save the images as .jpg, e.g.,
plt.savefig (r"D:\DeleteMe\20\test.png")