# from utils.secretStore import SecretStore
# user = SecretStore()
# decrypted_text = user.decrypt()
# print(decrypted_text)
#
# from utils.helperFunctions import SentimentAnalysis
#
# sa = SentimentAnalysis()
#
# res_ = sa.get_sentiment("SoftBank Group Corp. sold a majority of its stake in Paytm before regulatory scrutiny caused the once-celebrated Indian fintech firm’s shares to dive, according to the Vision Fund’s executive managing partner, as per a Bloomberg report.The Tokyo-based tech investor saw uncertainty growing in India’s regulatory environment, as well as over Paytm Payments Bank Ltd.’s license, Navneet Govil told Bloomberg News on February 8.“We felt it was prudent to start monetizing, the Vision Fund’s finance chief said, as quoted by Bloomberg.Were glad we did a good portion of Paytm before the recent stock correction.According to a Bloomberg analysis of company filings, SoftBank has been consistently selling off Paytm shares since at least November 2022 until last month. The Japanese investors stake in Paytm stood at approximately 5% as of January, a significant decrease from the approximately 18.5% stake it held around the time of Paytms initial public offering in 2021.When asked about SoftBanks plans regarding its remaining stake, Govil declined to comment.Earlier Paytm has received multiple warnings from regulators over the past two years regarding transactions between its popular payments app and its banking arm. Consequently, much of the banking operations business has been suspended by the Reserve Bank of India, leading to a decline of over 40% in Paytms stock price from its peak in January, as reported by Bloomberg.SoftBank earlier reported its first profit following four quarters of losses, with its Vision Fund also logging a profit in the December quarter. New bets by the startup investment arm have dwindled to a fraction of the billions it once wielded and have been outpaced by exit activity, however.Milestone Alert! Livemint tops charts as the fastest growing news website in the world 🌏 Click here to know more.Here’s your comprehensive 3-minute summary of all the things Finance Minister Nirmala Sitharaman said in her Budget speech: Click to download!")
# print(res_[0])


from utils.webscraping import GoogleNews
from utils.helpers import convertToPdf

gnews = GoogleNews()
res = gnews.get_news(sentiment=True, query="Paypal", max_results=50)

convertToPdf(res, "CP")


# import pickle
# file = open('BLTD.txt', 'wb')
# pickle.dump(res, file)
# file.close()

# for i in res:
#     print(i)

# from nlpretext import Preprocessor
# text = "nkmk;. m,k nd 😀 #food #paris \n </div>"
# preprocessor = Preprocessor()
# text = preprocessor.run(text)
# print(text)


# import pickle
#
# # open a file, where you stored the pickled data
# file = open('res.txt', 'rb')
#
# # dump information to that file
# data = pickle.load(file)
#
# # close the file
# file.close()

# from utils.helpers import SentimentAnalysis
#
# sa = SentimentAnalysis()
# sa.get_sentiment(data[0]["Text"].decode('utf-8'))
#
# print(sa.label)

