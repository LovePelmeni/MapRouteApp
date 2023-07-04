<div style="text::center"> 
  <h2>Map Route App Project</h2>
</div>

<div class="container badges" 
style="display: flex; justify-content: center; column-gap: 5px; margin-bottom: 30px">

<a href="https://github.com/badges/shields/pulse" alt="Activity">
        <img src="https://img.shields.io/badge/version-1.2.3-blue" /></a>

<a href="https://github.com/badges/shields/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/badges/shields" /></a>
    
<a href="https://circleci.com/gh/badges/shields/tree/master">
    <img src="https://img.shields.io/circleci/project/github/badges/shields/master" alt="build status">
</a>
    
<a href="https://circleci.com/gh/badges/daily-tests">
    <img src="https://img.shields.io/circleci/project/github/badges/daily-tests?label=service%20tests" alt="service-test status">
</a>

<a href="https://coveralls.io/github/badges/shields">
    <img src="https://img.shields.io/coveralls/github/badges/shields"
            alt="coverage">
</a>

</div>

---
#### ~ API Documentation [API Docs]("http://localhost:8000/swagger")

This Project was actually developed by myself pretty long time ago, but now it is fully deployed, 
well-documented, and fixed for all the bugs, that I was facing.

### *This application is the concept/prototype of the map routing system, that people asked me to build for their business purpose*

#### This App allows to get the optimal root to the destination with `Time` and `Distance` specified

<p align="center">
  <a href="*"><img src="./demo/demo.png" alt="FastAPI"></a>

---

## *Requirements*

~ `docker` - `1.3.8 or higher`

~ `docker-compose` - `3.8 or higher`

~ `OS` - Tested on `MacOS and Windows`

---

# Technologies 

`Languages` ~  `Python`, `Javascript`, `HTML`

`Frameworks & Main Libraries` ~ `Django Framework`, `LeafletJS`

`Databases & storages` - `PostgresSQL` & `Redis` 

`Webservers & Deployment Tool` - `Nginx`, `Docker`, `Docker-Compose`

--- 
# *Usage*

1. #### Fork this repo into your account.
2. #### Clone the repo to your local dev environment.
```doctest
    $ git clone <link to the repository>
```
3. #### Go to the `root` directory and start `docker-compose.yaml` file 

```doctest
    $ docker-compose up -d
```
4. #### Once it deployed, Go to the browser and check for it.

### Using Curl tool
```doctest
    $ curl -f http://localhost:8000
```
---
## ~ *Extra Links*

#### My LinkedIn ~ `https://linkedin/in/kirill-klimushin`

#### Emails for contributions ~ `kirklimushin@gmail.com` & `klimkiruk@gmail.com`
