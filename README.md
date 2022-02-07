<div id="top"></div>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://repository-images.githubusercontent.com/281412830/36e8ef00-cf2b-11ea-8ed3-a0d9baedd3b6" alt="Logo">
  </a>

  <h3 align="center">Twitter Get Post Client</h3>
  <p>
    <a href="https://github.com/ivansvit/twitter-client-get-post-tweet/issues">Report Bug</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

“Twitter Get Post Client” is an utility that allows users:
- get tweet by “id” 
- create tweet
- search tweet by keyword in last 24h

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://python.org/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Below you will find instructions of how you may setting up the project locally.
To get a local copy up and running follow these simple= steps.
<br>

### Prerequisites
<ol>
  <li><b>Twitter Credentials.</b> You can use this client <b>only</b> with your own twitter credentials.</li>
  <li><b>Knowledge.</b> This Client for beginners in programming.</li>
  <li><b>Operating system.</b> You can run the client on Windows, MacOS, Linux.</li>
  <li><b>Framework.</b> You can use any framework you like for development with Python.</li>
</ol>
<br>

### Installation


<ol>
  <li>Create a new project in your framework. I use PyCharm.</li>
  <li>Create a new file, for example “main.py”.</li>
  <li>If you already have a "main.py" file created and it already has a welcome script in it, delete that script.</li>
  <li>Copy code from my file “main.py” to your file</li>
  <li>Copy “requirements.txt” file to your project</li>
  <li>Install all packages from requirements.txt</li>
  
```
pip install -r requirements.txt
```

  <li>Register your twitter account as a developer. Follow the instruction from this <a href="https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api">Link</a>.</li>
  <li>Generate and Get your Twitter Developer credentials: </li>
    <ul>
      <li>API Key</li>
      <li>API Key Secret</li>
      <li>Bearer Token</li>
      <li>Access Token<</li>
      <li>Access Token Secret</li>
    </ul>
    <br>
    <img src="https://user-images.githubusercontent.com/46112066/152699894-8f0a1fe8-dd5c-4d64-8ffd-43966f36eba3.png">

  <li>Insert your Twitter dev credentials to the code in “main.py” file.</li>

```
  API_KEY = os.environ.get("API_KEY")
  API_KEY_SECRET = os.environ.get("API_KEY_SECRET")
  BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
  ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
  ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")
```

  <li>Finally you can try to call functions. You can test get_tweet_by_id() function with this id “1490336052627841025”.

```
  get_tweet_by_id(tweet_id="1490336052627841025") 
```
  You’ll receive this data as a response: 
 
```
  Response(data=<Tweet id=1490336052627841025 text=@kudrinko97 Florence? One of my favourite cities that I have ever visited>, includes={}, errors=[], meta={})
```
      
  If so all your credentials and code works well.</li>
 </ol>

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

```
# Call the function
get_tweet_by_id(tweet_id="1490336052627841025")
create_tweet(tweet_text="New Tweet")
get_tweets_by_keyword(keyword="Florence")
```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Ivan Svit - i.svit@yahoo.com

Project Link: [Twitter Get Post Client](https://github.com/ivansvit/twitter-client-get-post-tweet)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: https://repository-images.githubusercontent.com/281412830/36e8ef00-cf2b-11ea-8ed3-a0d9baedd3b6

