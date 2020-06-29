import facebook
import requests
from allauth.socialaccount.models import SocialAccount, SocialToken
from django.shortcuts import render
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from textblob import TextBlob
import io
import urllib,base64
from io import BytesIO



def sentiment_pie_chart(request):
    data=SocialAccount.objects.get(user=request.user.id)
    uid=data.uid
    data_token=SocialToken.objects.get(account=data.id)
    user_token=data_token.token
    long_lived_user_token=requests.get("https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=1056226111381872&client_secret=43d34975fdfcb00842bb55306264b0d8&fb_exchange_token={0}".format(user_token)).json()
    long_user_token=long_lived_user_token['access_token']

    graph = facebook.GraphAPI(access_token=long_user_token, version="3.0")
    po = graph.get_connections(uid, 'accounts')
    for i in po["data"]:
        page_token = i['access_token']
        page_id=i['id']
        page_name=i['name']
    graph = facebook.GraphAPI(page_token)
    profile = graph.get_object(page_id)
    posts = graph.get_connections(profile['id'], 'posts')
    comments = []
    message = []
    for post in posts["data"]:
        first_comments = graph.get_connections(id=post["id"], connection_name="comments")
        comments.extend(first_comments["data"])
    for comment in comments:
        message.append(comment["message"])
    # message = ['Nice☺️', 'True', 'Worst', 'Really!!!', 'Nice', 'Nice☺️', 'True', 'Worst', 'Really!!!', 'Nice',
    #            'Looks are awesome.', 'Battery backup is excellent.',
    #            ' Camera is good.The display light quality is good.',
    #            'Although this is good mobile, looks good, but Problem is that it doesn’t provide separate Space for dual SIM & memory card together.',
    #            'Not good one as expected.', ' Camera quality very poor.', 'today is a rainy day', 'ok',
    #            'yes please,but promote whole newsdn']

    positive_pol = 0
    negative_pol = 0
    neutral_pol = 0

    for m in message:
        analysis = TextBlob(m)
        x = analysis.sentiment.polarity
        if (x > 0):
            positive_pol += x

        elif (x < 0):
            negative_pol += x
        else:
            neutral_pol += 1
    data = []
    color=['#4CAF50', '#FA4443', '#2983FF']
    data.append(positive_pol)
    data.append(abs(negative_pol))
    data.append(neutral_pol)
    result = ["Positive", "Negative", "Neutral"]
    plt.pie(data, labels=result,colors=color, startangle=90, autopct='%1.1f%%')
    centre_circle=plt.Circle( (0,0), 0.7, color='white',linewidth=1.25)
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    data = graphic.decode('utf-8')
    plt.close()

    return render(request,'sentiment/pie_chart.html',{'data':data,'page_name':page_name})

    # word cloud
    # message = ['Nice☺️', 'True', 'Worst', 'Really!!!', 'Nice', 'Nice☺️', 'True', 'Worst', 'Really!!!',
    #            'Nice.looking awesome.do something better.best dale ever.wow.hfgxcbjchfdhkdfhih', 'Looks are awesome.',
    #            'Battery backup is excellent.', ' Camera is good.The display light quality is good.',
    #            'Although this is good mobile, looks good, but Problem is that it doesn’t provide separate Space for dual SIM & memory card together.',
    #            'Not good one as expected.', ' Camera quality very poor.', 'today is a rainy day', 'ok',
    #            'yes please,but promote whole newsdn']
    # # tagcloud
    # comment_words = ' '
    # stopwords = set(STOPWORDS)
    # for words in message:
    #     comment_words = comment_words + words + ' '
    #
    # wordcloud = WordCloud(width=800, height=800,
    #                       background_color='white',
    #                       stopwords=stopwords,
    #                       min_font_size=10).generate(comment_words)
    #
    # # plot the WordCloud image
    # plt.figure(figsize=(8, 8), facecolor=None)
    # plt.imshow(wordcloud)
    # plt.axis("off")
    # plt.tight_layout(pad=0)
    #
    # plt.show()
    # buffer = BytesIO()
    # plt.savefig(buffer, format='png')
    # buffer.seek(0)
    # image_png = buffer.getvalue()
    # buffer.close()
    #
    # graphic = base64.b64encode(image_png)
    # cloud = graphic.decode('utf-8')
    # plt.close()


    # return render(request,'sentiment/pie_chart1.html',{'data':data})



def tag_cloud(request):
    data=SocialAccount.objects.get(user=request.user.id)
    uid=data.uid
    data_token=SocialToken.objects.get(account=data.id)
    user_token=data_token.token
    long_lived_user_token=requests.get("https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=1056226111381872&client_secret=43d34975fdfcb00842bb55306264b0d8&fb_exchange_token={0}".format(user_token)).json()
    long_user_token=long_lived_user_token['access_token']

    graph = facebook.GraphAPI(access_token=long_user_token, version="3.0")
    po = graph.get_connections(uid, 'accounts')
    for i in po["data"]:
        page_token = i['access_token']
        page_id=i['id']
        page_name=i['name']
    graph = facebook.GraphAPI(page_token)
    profile = graph.get_object(page_id)
    posts = graph.get_connections(profile['id'], 'posts')
    comments = []
    message = []
    for post in posts["data"]:
        first_comments = graph.get_connections(id=post["id"], connection_name="comments")
        comments.extend(first_comments["data"])
    for comment in comments:
        message.append(comment["message"])
    # message = ['Nice☺️', 'True', 'Worst', 'Really!!!', 'Nice', 'Nice☺️', 'True', 'Worst', 'Really!!!',
    #            'Nice.looking awesome.do something better.best dale ever.wow.hfgxcbjchfdhkdfhih', 'Looks are awesome.',
    #            'Battery backup is excellent.', ' Camera is good.The display light quality is good.',
    #            'Although this is good mobile, looks good, but Problem is that it doesn’t provide separate Space for dual SIM & memory card together.',
    #            'Not good one as expected.', ' Camera quality very poor.', 'today is a rainy day', 'ok',
    #            'yes please,but promote whole newsdn']
    # tagcloud
    comment_words = ' '
    stopwords = set(STOPWORDS)
    for words in message:
        comment_words = comment_words + words + ' '

    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          stopwords=stopwords,
                          min_font_size=10).generate(comment_words)

    # plot the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.show()
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    cloud = graphic.decode('utf-8')
    plt.close()
    # return render(request,'sentiment/pie_chart1.html',{'data':data})
    return render(request, 'sentiment/tag_cloud.html', {'cloud': cloud,'page_name':page_name})