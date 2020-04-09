import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats.mstats import winsorize
from scipy.stats import zscore

states = pd.read_csv("states_all.csv")
states = states.interpolate()


#Toplam gelir verilerini içeren TOTAL_REVENUE ve toplam harcama verilerini içeren
# TOTAL_EXPENDITURE değişkenlerini inceleyin. Bu değişkenler aykırı değerler içeriyor mu?

# print(states["TOTAL_REVENUE"].head(10))
# print(states["TOTAL_REVENUE"].tail(10))
# print(states["TOTAL_REVENUE"].describe())
#
# plt.subplot(1,2,1)
# plt.boxplot(states["TOTAL_REVENUE"])
# plt.title("Total revenue kutu grafiği ")
# plt.subplot(1,2,2)
# plt.boxplot(states["TOTAL_EXPENDITURE"])
# plt.title("TOTAL_EXPENDITURE kutu grafiği ")
# plt.show()
#
# plt.subplot(121)
# plt.hist(states["TOTAL_REVENUE"])
# plt.title("Total revenue histogramı")
# plt.subplot(122)
# plt.hist(states["TOTAL_EXPENDITURE"])
# plt.title("TOTAL_EXPENDITURE histogramı")
# plt.show()
#
# z_scores = zscore(states["TOTAL_REVENUE"])
# for threshold in range(1,5):
#     print("Eşik değeri: {}".format(threshold))
#     print("Aykırı değerlerin sayısı: {}".format(len((np.where(z_scores > threshold)[0]))))
#     print('------')

#--------------------------------------------------------------------------------------------------------------

#Toplam gelir (TOTAL_REVENUE) ve toplam harcama (TOTAL_EXPENDITURE) değişkenlerinde aykırı değer
# tespit ettiyseniz bu derste öğrendiğiniz teknikleri uygulayarak
# bu aykırı değerleri ortadan kaldırın ve bunu yaptıktan sonra hiçbir aykırı değer kalmadığını doğrulayın.

# print(states["TOTAL_REVENUE"].head(5))
#
# winsorize_total_revenue = winsorize(states["TOTAL_REVENUE"], (0, 0.109))
#
#
# plt.boxplot(winsorize_total_revenue)
# plt.title("winsorized total revenue")
# plt.show()
#
# plt.figure(figsize = (12,5))
# plt.subplot(1,2,1)
# plt.hist(states["TOTAL_REVENUE"])
# plt.title(" TOTAL_REVENUE sayısı")
#
# plt.subplot(1,2,2)
# plt.hist(np.log(states["TOTAL_REVENUE"]))
# plt.title("TOTAL_REVENUE Sayısı (log dönüşümlü)")
# plt.show()
#
# plt.figure(figsize = (12,5))
#
# plt.subplot(1,2,1)
# plt.boxplot(states["TOTAL_REVENUE"])
# plt.title(" TOTAL_REVENUE sayısı")
#
# plt.subplot(1,2,2)
# plt.boxplot(np.log(states["TOTAL_REVENUE"]))
# plt.title("TOTAL_REVENUE Sayısı (log dönüşümlü)")
# plt.show()


# winsorize_total_expenditure = winsorize(states["TOTAL_EXPENDITURE"], (0, 0.106))

# plt.subplot(121)
# plt.boxplot(states["TOTAL_EXPENDITURE"])
# plt.title("Total expenditure")
#
# plt.subplot(122)
# plt.boxplot(winsorize_total_expenditure)
# plt.title("winsorized total expenditure")
# plt.show()

#------------------------------------------------------------------------------------------------------

#Toplam gelir (TOTAL_REVENUE) değişkeninden, toplam harcama (TOTAL_EXPENDITURE) değerini çıkartarak
# bütçe açığı olarak düşünülebilecek bir değişken oluşturun (aykırı değerleri temezlemeden).
# Bu yeni değişkende de aykırı değerler yer almakta mı? Varsa bu aykırı değerleri de temizley0in.


#excel dosyasına ekleyip yapmak istedim değişik bir şeyler olsun diye.
#
#
# butce = []
#
# for i in range (len(states)):
#     butce.append(states["TOTAL_REVENUE"][i]-states["TOTAL_EXPENDITURE"][i])
#

# states["butce"] = butce
#
# plt.figure(figsize=(12,5))
# plt.subplot(121)
# plt.boxplot(states["butce"])
# plt.title("total revenue - total expenditure (butce)")
#
# winsorize_butce = winsorize(states["butce"], (0.161, 0.12))
# plt.subplot(122)
# plt.boxplot(winsorize_butce)
# plt.title("Winsorized total revenue - total expenditure (butce)")
# plt.show()

# #----------------------------------------------------------------------

#Yine toplam gelir (TOTAL_REVENUE) değişkeninden, toplam harcama(TOTAL_EXPENDITURE)
# değerini çıkartarak bütçe açığı olarak düşünülebilecek bir değişken oluşturun.
# Fakat bu sefer aykırı değerleri temezledikten sonra bu işlemi yapın.
# Bu yeni değişkende de aykırı değerler var mı? Varsa bunları da temizlemekte fayda var.
#
#
# winsorize_total_revenue = winsorize(states["TOTAL_REVENUE"], (0, 0.109))
#
# winsorize_total_expenditure = winsorize(states["TOTAL_EXPENDITURE"], (0, 0.106))
#
# butce2 = []
#
# for i in range (len(states)):
#      butce2.append(winsorize_total_revenue[i]-winsorize_total_expenditure[i])
#
#
# plt.figure(figsize=(12,5))
# plt.subplot(121)
# plt.boxplot(butce2)
# plt.title("total revenue - total expenditure (butce2)")
#
# winsorize_butce = winsorize(butce2, (0.161, 0.12))
# plt.subplot(122)
# plt.boxplot(winsorize_butce)
# plt.title("Winsorized total revenue - total expenditure (butce2)")
# plt.show()

# ----------------------------------------------------------------------------------------------

#Şimdi elimizde üçüncü ve ve dördüncü sorularda oluşturduğumuz iki farklı bütçe değişkeni var.
# Bu ikisi arasında fark görüyor musunuz?

#bu soru için sadece line 97-100 arası ve 124-131 arasındaki commandi kaldırmak gerekiyor.

# plt.subplot(121)
# plt.boxplot(butce)
# plt.title("butce without winsorize revenue and expenditure")
#
# plt.subplot(122)
# plt.boxplot(butce2)
# plt.title("butce with winsorize revenur and expenditure")
# plt.show()

#winsorize olmayanda daha çok ayrık değer var.

#--------------------------------------------------------------------------------------------------------

#Bizim için bütçe açığı çok önemli bir değişken olsaydı
# aykırı değerleri temizlemek için hangi yöntem daha iyi olurdu.
# Üçüncü soruda uguladığınız yöntem mi yoksa dördüncü sorudaki yöntem mi?

#4. ayrık değerlerden daha çok kurtulmuş durumdayız.



