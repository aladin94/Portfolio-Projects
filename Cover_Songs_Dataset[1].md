
# Welcome to my Portfolio Project on WebScraping!

## In this project, I am going to analyze the Top 100 Covered Albums of All-Time. This project is definitely more personal to me as opposed to my other exercises. As an Amateur Musician, not only do I have a passion for music, but I most definitely love discovering covers of Songs/Albums where the artist provides his/her own twist to the original.


```python
#Make the necessary imports immediately to avoid errors.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
import requests 
from bs4 import BeautifulSoup 
```


```python
#Here we are making an HTTP request to pull the HTML code from the URL we desire.

URL = "https://secondhandsongs.com/statistics?sort=covers&list=stats_release_covers"
r = requests.get(URL) 
```


```python
soup = BeautifulSoup(r.content, "html5lib") 
print (soup.prettify())
```

    <!DOCTYPE html>
    <html class="no-js">
     <head>
      <meta charset="utf-8"/>
      <title>
       Database Statistics |  SecondHandSongs
      </title>
      <meta content="Find out who performed the original version of a particular song, or who covered or sampled that song. Unlike many related
                          sites, we try to be as complete as possible (not just performer and song title, but also songwriters and original releases) and order the data in a reusable and maintainable way." name="description"/>
      <meta content="Covers, Cover Songs, Samples, Tributes, Music" name="keywords"/>
      <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
      <link href="/art/apple-touch-icon-precomposed.png" rel="apple-touch-icon-precomposed"/>
      <link href="/art/apple-touch-icon-72x72-precomposed.png" rel="apple-touch-icon-precomposed" sizes="72x72"/>
      <link href="/art/apple-touch-icon-76x76-precomposed.png" rel="apple-touch-icon-precomposed" sizes="76x76"/>
      <link href="/art/apple-touch-icon-114x114-precomposed.png" rel="apple-touch-icon-precomposed" sizes="114x114"/>
      <link href="/art/apple-touch-icon-120x120-precomposed.png" rel="apple-touch-icon-precomposed" sizes="120x120"/>
      <link href="/art/apple-touch-icon-144x144-precomposed.png" rel="apple-touch-icon-precomposed" sizes="144x144"/>
      <link href="/art/apple-touch-icon-152x152-precomposed.png" rel="apple-touch-icon-precomposed" sizes="152x152"/>
      <link href="/art/favicon.png" rel="icon"/>
      <!--[if IE]>
                <link rel="shortcut icon" href="/favicon.ico"><![endif]-->
      <!-- or, set /favicon.ico for IE10 win -->
      <meta content="#0b9dae" name="msapplication-TileColor"/>
      <meta content="/art/tileicon.png" name="msapplication-TileImage"/>
      <link href="/rss/new.xml" rel="alternate" title="Second Hand Songs new submissions (RSS 2.0)" type="application/rss+xml"/>
      <link href="//fonts.googleapis.com/css?family=Open+Sans:300italic,600italic,400,300,600,700,800&amp;subset=latin,cyrillic-ext,greek-ext,greek,vietnamese,latin-ext,cyrillic" rel="stylesheet" type="text/css"/>
      <link href="/build/css/app.d7e0b924f1765da44b69a19c11a49cda.css" rel="stylesheet"/>
      <script type="text/javascript">
       window.cookieconsent_options = {"message":"We use cookies to personalise content and ads, to provide social media features and to analyse our traffic. We also share information about your use of our site with our social media, advertising and analytics partners","dismiss":"Got it","learnMore":"Learn more","link":"https://secondhandsongs.com/page/CookiePolicy","theme":"dark-top"};
      </script>
      <script async="" src="//cdnjs.cloudflare.com/ajax/libs/cookieconsent2/1.0.9/cookieconsent.min.js" type="text/javascript">
      </script>
     </head>
     <body class="">
      <div class="loading">
       <div class="loader">
       </div>
      </div>
      <input name="_ds" type="hidden" value="0"/>
      <section id="header">
       <header class="container">
        <div class="row">
         <div class="d-none d-md-block col-lg-4 col-md-5">
          <a class="logo" href="/">
           <img alt="Second Hand Songs - A Cover Songs Database" src="/art/logo.png"/>
          </a>
         </div>
         <nav class="navbar navbar-expand navbar-dark col-lg-8 col-md-7" id="top-menu">
          <ul class="nav navbar-nav navbar-right" id="top-menu-navbar-collapse">
           <li class="nav-item d-block d-md-none">
            <a class="nav-link logo" href="/">
             <img alt="Second Hand Songs - A Cover Songs Database" src="/art/logo.png"/>
            </a>
           </li>
           <li class="nav-item">
            <a class="nav-link" href="/explore">
             Explore
            </a>
           </li>
           <li class="nav-item">
            <a class="nav-link" href="/forum">
             Discuss
            </a>
           </li>
           <li class="nav-item">
            <a class="nav-link" href="/participate">
             Participate
            </a>
           </li>
           <li class="nav-item">
            <a class="nav-link" href="/quiz">
             Play
            </a>
           </li>
           <li class="nav-item accent">
            <a class="nav-link" href="/login?ref=%2Fstatistics%3Fsort%3Dcovers%26list%3Dstats_release_covers">
             Sign In
            </a>
           </li>
           <li class="nav-item social">
            <a class="nav-link" href="https://www.facebook.com/pages/SecondHandSongs/25077961981" title="Like us on Facebook">
             <i class="fa fa-facebook-square fa-lg ">
             </i>
            </a>
            <a class="nav-link" href="https://twitter.com/SHSongs" title="Follow us on twitter">
             <i class="fa fa-twitter-square fa-lg ">
             </i>
            </a>
           </li>
          </ul>
         </nav>
        </div>
       </header>
      </section>
      <section id="topsearch">
       <div class="container">
        <form action="/search" class="form-inline row align-items-center" id="topsearch-form">
         <div class="d-none d-sm-block col-sm-3">
          <h2 class="text-right">
           Discover
          </h2>
         </div>
         <div class="col col-sm-6">
          <div class="input-group">
           <input class="form-control" id="topsearch-input" name="search_text" placeholder="Find cover songs, artists and more" tabindex="1" type="text" value=""/>
           <div class="input-group-btn">
            <button accesskey="z" class="btn" id="topsearch-button">
             Go
            </button>
           </div>
          </div>
         </div>
         <div class="d-none d-sm-block col-sm-3">
          <a class="section-more" href="/search/work">
           Detailed search
          </a>
         </div>
        </form>
       </div>
      </section>
      <section id="alert">
       <section class="alert-danger">
        <div class="container" id="alert-container">
         <div class="errormsg alert" style="display:none;">
          <h4>
           Error!
          </h4>
          <p class="my-0">
          </p>
         </div>
        </div>
       </section>
       <section class="alert-warning">
        <div class="container">
         <div class="warning alert" style="display:none;">
          <h4>
           Warning
          </h4>
          <p>
          </p>
          <input class="btn btn-secondary" name="override" type="button" value="Confirm"/>
         </div>
        </div>
       </section>
       <section class="alert-success">
        <div class="container">
         <div class="successmsg alert" style="display:none;">
         </div>
        </div>
       </section>
      </section>
      <section id="main">
       <section id="content-tabs">
        <div class="container">
         <div class="row">
          <div class="col-sm-12">
           <ul class="nav nav-tabs nav-justified" id="nav-entity">
            <li class="nav-item">
             <a class="nav-link " href="/explore">
              <i class="fa fa-compass fa- ">
              </i>
              Explore the database
             </a>
            </li>
            <li class="nav-item">
             <a class="nav-link active" href="/statistics">
              <i class="fa fa-bar-chart-o fa- ">
              </i>
              Database statistics
             </a>
            </li>
           </ul>
          </div>
         </div>
        </div>
       </section>
       <section id="content-section">
        <div class="container">
         <div class="row">
          <div class="col-sm-12">
           <div class="controller" data-model="yzV7phQBJnojZasrIQku-YAY5pt4-IfYkXd67F-gpnH50BPapQND-sLjHVe2i1Gn46Da_fDqI-sNi9gqubFxOOLPckuU5oO997AWosENmBBgm-nKzfZUnemazTdBznj9M5g2wkdIVwa43EZHr270nIWC-raWzzKeeRYjqcd4eIzjgniV1KI2qUEw49IGlsCf.OvXZg0n83lRPhEcxQLAuSQ==" data-service="shs.control.browser.statistics" data-url="/statistics" id="root_wrapper">
            <div id="root">
             <section class="my-3">
              <ul class="nav nav-pills nav-justified">
               <li class="nav-item dropdown">
                <a aria-expanded="false" aria-haspopup="true" class="nav-link" data-toggle="dropdown" href="#" id="browse-song" role="button">
                 Song statistics
                </a>
                <div aria-labelledby="browse-song" class="dropdown-menu">
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_work_covered&amp;sort=covers" id="list_stats_work_covered">
                  Most covered songs
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_most_covered_work_per_original_year&amp;sort=covers" id="list_stats_most_covered_work_per_original_year">
                  Most covered songs per original year
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_most_covered_work_per_cover_year&amp;sort=covers" id="list_stats_most_covered_work_per_cover_year">
                  Most covered songs per cover year
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_most_sampled_recording&amp;sort=covers" id="list_stats_most_sampled_recording">
                  Most sampled recordings
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_performance_rating&amp;sort=covers" id="list_stats_performance_rating">
                  Best/worst rated performances
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_covers_per_year&amp;sort=covers" id="list_stats_covers_per_year">
                  Number of covers per year
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_samples_per_year&amp;sort=covers" id="list_stats_samples_per_year">
                  Number of samples per year
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_most_used_language&amp;sort=covers" id="list_stats_most_used_language">
                  Most used languages
                 </a>
                </div>
               </li>
               <li class="nav-item dropdown">
                <a aria-expanded="false" aria-haspopup="true" class="nav-link" data-toggle="dropdown" href="#" id="browse-artist" role="button">
                 Artist statistics
                </a>
                <div aria-labelledby="browse-artist" class="dropdown-menu">
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_most_covered_author&amp;sort=covers" id="list_stats_most_covered_author">
                  Most covered authors
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_most_covered_performer&amp;sort=covers" id="list_stats_most_covered_performer">
                  Most covered performers
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_most_covering_performer&amp;sort=covers" id="list_stats_most_covering_performer">
                  Most covering performers
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_most_sampled_performer&amp;sort=covers" id="list_stats_most_sampled_performer">
                  Most sampled performers
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_most_sampling_performer&amp;sort=covers" id="list_stats_most_sampling_performer">
                  Most sampling performers
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_most_tributed_artist&amp;sort=covers" id="list_stats_most_tributed_artist">
                  Most tributed artists
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_artist_rating&amp;sort=covers" id="list_stats_artist_rating">
                  Best/worst rated artists
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_country_artists&amp;sort=covers" id="list_stats_country_artists">
                  Countries with most artists
                 </a>
                </div>
               </li>
               <li class="nav-item dropdown">
                <a aria-expanded="false" aria-haspopup="true" class="nav-link" data-toggle="dropdown" href="#" id="browse-release" role="button">
                 Release statistics
                </a>
                <div aria-labelledby="browse-release" class="dropdown-menu">
                 <a class="dropdown-item refresh-click active" href="/statistics?list=stats_release_covers&amp;sort=covers" id="list_stats_release_covers">
                  Most covered releases
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_label_releases&amp;sort=covers" id="list_stats_label_releases">
                  Labels with most releases
                 </a>
                </div>
               </li>
               <li class="nav-item dropdown">
                <a aria-expanded="false" aria-haspopup="true" class="nav-link" data-toggle="dropdown" href="#" id="browse-growth" role="button">
                 Growth statistics
                </a>
                <div aria-labelledby="browse-growth" class="dropdown-menu">
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_performances_over_time&amp;sort=covers" id="list_stats_performances_over_time">
                  Performances over time
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_works_over_time&amp;sort=covers" id="list_stats_works_over_time">
                  Works over time
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_videos_over_time&amp;sort=covers" id="list_stats_videos_over_time">
                  Videos over time
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_webcovers_over_time&amp;sort=covers" id="list_stats_webcovers_over_time">
                  Web covers over time
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_users_over_time&amp;sort=covers" id="list_stats_users_over_time">
                  Users over time
                 </a>
                </div>
               </li>
               <li class="nav-item dropdown">
                <a aria-expanded="false" aria-haspopup="true" class="nav-link" data-toggle="dropdown" href="#" id="browse-user" role="button">
                 User statistics
                </a>
                <div aria-labelledby="browse-user" class="dropdown-menu">
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_user_submissions&amp;sort=covers" id="list_stats_user_submissions">
                  Most submitting
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_user_videos&amp;sort=covers" id="list_stats_user_videos">
                  Most videos added
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_user_web_covers&amp;sort=covers" id="list_stats_user_web_covers">
                  Most web covers added
                 </a>
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_users_born&amp;sort=covers" id="list_stats_users_born">
                  Users per birth year
                 </a>
                </div>
               </li>
               <li class="nav-item dropdown">
                <a aria-expanded="false" aria-haspopup="true" class="nav-link" data-toggle="dropdown" href="#" id="browse-other" role="button">
                 Other statistics
                </a>
                <div aria-labelledby="browse-other" class="dropdown-menu">
                 <a class="dropdown-item refresh-click " href="/statistics?list=stats_external_links_per_source_type&amp;sort=covers" id="list_stats_external_links_per_source_type">
                  External links
                 </a>
                </div>
               </li>
              </ul>
             </section>
             <section class="mt-3">
              <h2 id="titleHeader">
               Most covered releases
              </h2>
              <p>
              </p>
              <div id="root_filter" style="display:none;">
              </div>
              <div id="pt" style="display:none;">
              </div>
              <table class="table data object table-striped" id="vw">
               <thead>
                <tr>
                 <th class="field-index ">
                 </th>
                 <th class="field-release ">
                  Release
                 </th>
                 <th class="field-performer ">
                  Performer
                 </th>
                 <th class="field-covers text-right">
                  Covers
                  <i class="fa fa-caret-down fa- ">
                  </i>
                 </th>
                </tr>
               </thead>
               <tbody>
                <tr>
                 <td class="field-index ">
                  1
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/712">
                   The Beatles [White Album]
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/41">
                   The Beatles
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  1634
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  2
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/156">
                   Rubber Soul
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/41">
                   The Beatles
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  1497
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  3
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/1095">
                   Revolver
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/41">
                   The Beatles
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  1489
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  4
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/243">
                   Abbey Road
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/41">
                   The Beatles
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  1468
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  5
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/152911">
                   Meet Me in St. Louis
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/1424+35156">
                   Judy Garland with Georgie Stoll and His Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  1399
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  6
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/133079">
                   Silent Night, Hallowed Night
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/56262">
                   Haydn Quartet
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  1378
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  7
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/28177">
                   The Christmas Song (Merry Christmas to You)
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/52045">
                   The King Cole Trio with String Choir
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  1195
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  8
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/31">
                   Sgt. Pepper's Lonely Hearts Club Band
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/41">
                   The Beatles
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  1107
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  9
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/888">
                   Help!
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/41">
                   The Beatles
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  1081
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  10
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/18821">
                   Were You Fooling
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/21999">
                   Richard Himber &amp; His Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  996
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  11
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/40215">
                   Jingle Bells
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/56262">
                   Edison Male Quartette
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  985
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  12
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/74035">
                   Body and Soul
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/33606">
                   Ambrose and His Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  955
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  13
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/83570">
                   God Rest Ye Merry, Gentlemen
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/64422">
                   Meister Glee Singers
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  901
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  14
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/418">
                   A Hard Day's Night
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/41">
                   The Beatles
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  891
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  15
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/84167">
                   The First Nowell
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/64817">
                   Tally-Ho!
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  839
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  16
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/35932">
                   I'll Be Home for Christmas (If Only in My Dreams)
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/243+26334">
                   Bing Crosby with John Scott Trotter and His Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  830
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  17
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/799">
                   The Freewheelin' Bob Dylan
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/158">
                   Bob Dylan
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  801
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  18
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/83498">
                   Christmas with The Trapp Family Singers
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/64386">
                   The Trapp Family Singers
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  794
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  19
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/34564">
                   Somebody's Gotta Go
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/6877">
                   Cootie Williams and His Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  738
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  20
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/4363">
                   O Amor o Sorriso e a Flor
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/3058">
                   João Gilberto
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  715
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  21
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/17479">
                   Let It Snow! Let It Snow! Let It Snow!
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/17403">
                   Vaughn Monroe and His Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  701
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  22
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/4777">
                   Tapestry
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/2270">
                   Carole King
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  667
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  23
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/40079">
                   One Night in Havana
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/1564">
                   Hoagy Carmichael &amp; His Pals
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  626
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  24
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/16746">
                   Caravan
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/112830">
                   Barney Bigard and His Jazzopators
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  620
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  25
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/15333">
                   Moon River
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/233">
                   Henry Mancini, His Orchestra and Chorus
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  619
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  26
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/64">
                   Bridge over Troubled Water
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/21291">
                   Simon and Garfunkel
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  606
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  27
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/24142">
                   Hesitating Blues
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/26565">
                   Prince's Band
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  599
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  28
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/156323">
                   St. Louis Woman - Original Broadway Cast
                  </a>
                 </td>
                 <td class="field-performer ">
                 </td>
                 <td class="field-covers text-right">
                  595
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  29
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/4357">
                   Kind of Blue
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/106">
                   Miles Davis
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  579
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  30
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/39342">
                   Georgia (On My Mind)
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/1564">
                   Hoagy Carmichael and His Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  564
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  31
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/80511">
                   Orfeu Negro - Bande Originale du Film de Marcel Camus
                  </a>
                 </td>
                 <td class="field-performer ">
                 </td>
                 <td class="field-covers text-right">
                  562
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  32
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/108">
                   Songs in the Key of Life
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/110">
                   Stevie Wonder
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  541
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  33
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/35590">
                   Lover Man (Oh, Where Can You Be?)
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/1496">
                   Billie Holiday
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  539
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  34
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/2545">
                   Giant Steps
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/2281">
                   John Coltrane
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  533
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  35
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/246700">
                   Love Letters
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/3545">
                   Victor Young and His Concert Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  531
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  36
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/26684">
                   Sleigh Ride
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/5234">
                   Boston Pops Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  529
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  37
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/38878">
                   Willow Weep for Me
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/8159">
                   Ted Fiorito &amp; His Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  527
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  38
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/760">
                   Imagine
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/143">
                   John Lennon
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  526
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  39
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/40506">
                   Rudolph, the Red-Nosed Reindeer
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/8191+137584">
                   Gene Autry and The Pinafores with Orchestral Accompaniment
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  524
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  40
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/25533">
                   Harlem on Parade
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/12006">
                   Gene Krupa &amp; His Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  511
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  41
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/72925">
                   Fools Rush In
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/11273">
                   Chick Bullock &amp; His Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  510
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  42
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/32899">
                   A Fine Romance
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/11997">
                   Guy Lombardo and His Royal Canadians
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  500
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  43
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/26980">
                   Yearning Just for You
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/19876">
                   Ben Bernie and His Hotel Roosevelt Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  499
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  44
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/2124">
                   Blue
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/5191">
                   Joni Mitchell
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  493
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  45
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/40077">
                   In a Sentimental Mood
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/4305">
                   Duke Ellington and His Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  488
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  46
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/52700">
                   Love Is Here to Stay
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/17024">
                   Ella Logan
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  486
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  47
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/115680">
                   A Shine on Your Shoes
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/11277">
                   Leo Reisman and His Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  483
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  48
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/94835">
                   Don't Do Something to Someone Else (That You Wouldn't Want Done to You)
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/6842">
                   Gordon Jenkins and His Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  482
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  49
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/18593">
                   A Charlie Brown Christmas
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/14385">
                   Vince Guaraldi
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  478
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  50
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/3295">
                   The Sandpiper - Original Motion Picture Soundtrack
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/3001">
                   Johnny Mandel
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  476
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  51
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/3005">
                   Talking Book
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/110">
                   Stevie Wonder
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  476
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  52
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/273">
                   Thriller
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/254">
                   Michael Jackson
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  475
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  53
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/38812">
                   What a Wonderful World
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/2823">
                   Louis Armstrong
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  473
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  54
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/18899">
                   Blue Christmas
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/22034">
                   Doye O'Dell
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  466
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  55
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/104207">
                   Poor Hawthorne
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/77226">
                   Ukrainian National Chorus
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  466
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  56
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/28175">
                   Nature Boy
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/320">
                   King Cole
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  463
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  57
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/20965">
                   I'll Follow You
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/6053+29799">
                   Paul Whiteman and His Orchestra with vocal refrain by Red McKenzie
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  463
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  58
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/10964">
                   Thelonious
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/2288">
                   Thelonious Monk Trio
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  461
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  59
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/7287">
                   West Side Story [OBC]
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/9531+41391+113126+113782">
                   Leonard Bernstein with Irwin Kostal and Sid Ramin – Original Broadway Cast
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  458
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  60
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/9274">
                   Equinox
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/500">
                   Sergio Mendes &amp; Brasil '66
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  457
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  61
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/98188">
                   Misty
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/2481">
                   Erroll Garner Trio
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  456
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  62
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/32376">
                   Cry Me a River
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/1246">
                   Julie London
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  449
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  63
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/2407">
                   Nevermind
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/169">
                   Nirvana [US]
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  447
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  64
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/112">
                   Blue Hawaii
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/103">
                   Elvis Presley
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  442
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  65
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/12842">
                   Hey Jude
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/41">
                   The Beatles
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  442
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  66
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/16739">
                   Turn on the Heat
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/20506">
                   Bert Stock and His Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  440
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  67
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/69028">
                   Fever
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/8029">
                   Little Willie John
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  434
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  68
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/140562">
                   "Tryout" - A Series of Private Rehearsal Recordings
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/3278+4029">
                   Kurt Weill and Ira Gershwin
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  434
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  69
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/100765">
                   They Can't Take That Away from Me
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/2232+11247">
                   Fred Astaire with Johnny Green and His Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  434
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  70
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/101382">
                   True
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/75527">
                   Al Bowlly
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  430
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  71
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/85842">
                   Angel Eyes
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/45892">
                   Herb Jeffries
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  427
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  72
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/89906">
                   Merry-Go-Round
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/4305">
                   Duke Ellington and His Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  426
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  73
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/3211">
                   The Sound of Music
                  </a>
                 </td>
                 <td class="field-performer ">
                 </td>
                 <td class="field-covers text-right">
                  423
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  74
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/18534">
                   Never No Lament
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/4305">
                   Duke Ellington and His Famous Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  418
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  75
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/13461">
                   Oh Lonesome Me
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/1415">
                   Don Gibson
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  418
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  76
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/21013">
                   Take the "A" Train
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/4305">
                   Duke Ellington and His Famous Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  416
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  77
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/1483">
                   Wildflowers
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/1421">
                   Judy Collins
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  412
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  78
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/704">
                   Various Positions
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/150">
                   Leonard Cohen
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  410
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  79
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/27100">
                   You Go to My Head
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/7542">
                   Larry Clinton &amp; His Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  409
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  80
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/162807">
                   Music from Beyond the Moon
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/11874+15990">
                   Vic Damone and Music by Camarata
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  405
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  81
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/153502">
                   When You Wish Upon a Star - I've Got No Strings
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/3545+3589+12173">
                   Cliff Edwards with Victor Young and His Orchestra and The Ken Darby Singers
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  398
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  82
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/3170">
                   The Wall
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/560">
                   Pink Floyd
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  398
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  83
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/97105">
                   You'd Be So Nice to Come Home To
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/11275">
                   Dick Jurgens and His Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  394
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  84
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/21374">
                   What the World Needs Now - Stan Getz Plays Bacharach and David
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/2205">
                   Stan Getz
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  391
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  85
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/31927">
                   New Britain
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/33303">
                   The Original Sacred Harp Choir
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  387
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  86
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/2467">
                   The Bootleg Series Volumes 1-3
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/158">
                   Bob Dylan
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  386
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  87
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/17987">
                   God Bless the Child
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/1496">
                   Billie Holiday
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  385
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  88
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/38917">
                   Don't Blame Me
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/979+3251">
                   Sarah Vaughan with George Treadwell's Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  381
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  89
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/4642">
                   The Joshua Tree
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/297">
                   U2
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  379
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  90
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/2749">
                   Comme d'habitude
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/2077">
                   Claude François
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  379
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  91
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/20932">
                   Carnegie Hall, November 13, 1948
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/4305">
                   Duke Ellington and His Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  378
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  92
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/83778">
                   Bye Bye Blackbird
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/19880">
                   Sam Lanin's Dance Orchestra
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  377
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  93
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/1985">
                   Innervisions
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/110">
                   Stevie Wonder
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  377
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  94
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/295">
                   Bringing It All Back Home
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/158">
                   Bob Dylan
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  376
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  95
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/96450">
                   Secret Love
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/401">
                   Doris Day
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  375
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  96
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/25790">
                   After You've Gone
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/19977+22089">
                   Henry Burr &amp; Albert Campbell
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  374
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  97
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/3143">
                   Saturday Night Fever
                  </a>
                 </td>
                 <td class="field-performer ">
                 </td>
                 <td class="field-covers text-right">
                  369
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  98
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/317">
                   Blonde on Blonde
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/158">
                   Bob Dylan
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  368
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  99
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/12838">
                   Let It Be
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/41">
                   The Beatles
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  368
                 </td>
                </tr>
                <tr>
                 <td class="field-index ">
                  100
                 </td>
                 <td class="field-release ">
                  <a class="link-release" href="/release/71704">
                   Dreamy Blues
                  </a>
                 </td>
                 <td class="field-performer ">
                  <a class="link-performer" href="/artist/4305">
                   The Jungle Band
                  </a>
                 </td>
                 <td class="field-covers text-right">
                  368
                 </td>
                </tr>
               </tbody>
              </table>
              <div id="pb" style="display:none;">
              </div>
              <div class="my-3" id="mp">
               <a class="refresh-click btn btn-secondary" href="/statistics?page=1&amp;sort=covers&amp;list=stats_release_covers" id="mp_1" name="mp_1">
                More
               </a>
              </div>
             </section>
            </div>
            <input name="root" type="hidden" value="yzV7phQBJnojZasrIQku-YAY5pt4-IfYkXd67F-gpnH50BPapQND-sLjHVe2i1Gn46Da_fDqI-sNi9gqubFxOOLPckuU5oO997AWosENmBBgm-nKzfZUnemazTdBznj9M5g2wkdIVwa43EZHr270nIWC-raWzzKeeRYjqcd4eIzjgniV1KI2qUEw49IGlsCf.OvXZg0n83lRPhEcxQLAuSQ=="/>
           </div>
          </div>
         </div>
        </div>
       </section>
      </section>
      <footer class="fill" id="footer">
       <div class="container">
        <div class="row">
         <section class="col-sm-6 col-md-3">
          <h2>
           <a href="/">
            <img alt="SecondHandSongs" class="img-responsive" src="/art/logo-alt-small.png"/>
           </a>
          </h2>
          <p class="lead">
           Discover
           <strong>
            The Original
           </strong>
          </p>
          <p>
           SecondHandSongs is building the most comprehensive source of cover song information.
          </p>
          <p>
          </p>
          <ul class="list-inline">
           <li class="list-inline-item">
            <a href="mailto:info@secondhandsongs.com" title="Send us an e-mail">
             <i class="fa fa-envelope fa-3x ">
             </i>
            </a>
           </li>
           <li class="list-inline-item">
            <a href="https://www.facebook.com/pages/SecondHandSongs/25077961981" title="Like us on Facebook">
             <i class="fa fa-facebook-square fa-3x ">
             </i>
            </a>
           </li>
           <li class="list-inline-item">
            <a href="https://twitter.com/SHSongs" title="Follow us on twitter">
             <i class="fa fa-twitter-square fa-3x ">
             </i>
            </a>
           </li>
          </ul>
         </section>
         <section class="col-sm-6 col-md-3 footer-links">
          <div class="text-content">
           <h2>
            About
           </h2>
           <ul>
            <li>
             <a href="/page/Introduction">
              Introduction
             </a>
            </li>
            <li>
             <a href="/page/FAQ">
              FAQ
             </a>
            </li>
            <li>
             <a href="/page/Glossary">
              Glossary
             </a>
            </li>
            <li>
             <a href="/page/MusicLicensing">
              Music licensing
             </a>
            </li>
            <li>
             <a href="/page/API">
              API
             </a>
            </li>
            <li>
             <a href="/page/Bookmarks">
              Bookmarks
             </a>
            </li>
            <li>
             <a href="/page/Copyright">
              Copyright
             </a>
            </li>
            <li>
             <a href="/page/Press">
              Press
             </a>
            </li>
            <li>
             <a href="/page/About">
              About us
             </a>
             <h2>
              Get involved
             </h2>
            </li>
            <li>
             <a href="/participate">
              Suggest covers and samples
             </a>
            </li>
            <li>
             <a href="/page/JoinUs">
              Join us
             </a>
            </li>
            <li>
             <a href="/page/Donate">
              Donate
             </a>
            </li>
            <li>
             <a href="/page/ContactUs">
              Contact us
             </a>
            </li>
           </ul>
          </div>
         </section>
         <section class="col-sm-6 col-md-3 footer-links">
          <h2>
           Popular performances
          </h2>
          <ul>
           <li>
            <a href="/performance/6392">
             Take Me Home, Country Roads
            </a>
           </li>
           <li>
            <a href="/performance/954">
             Heroes
            </a>
           </li>
           <li>
            <a href="/performance/26947">
             Simple Man
            </a>
           </li>
           <li>
            <a href="/performance/19702">
             Desperado
            </a>
           </li>
           <li>
            <a href="/performance/8314">
             Spirit in the Sky
            </a>
           </li>
           <li>
            <a href="/performance/2841">
             Crimson and Clover
            </a>
           </li>
           <li>
            <a href="/performance/16551">
             Forever Young
            </a>
           </li>
           <li>
            <a href="/performance/7446">
             Mad World
            </a>
           </li>
           <li>
            <a href="/performance/2085">
             Wild Horses
            </a>
           </li>
           <li>
            <a href="/performance/1051">
             Wicked Game
            </a>
           </li>
          </ul>
         </section>
         <section class="col-sm-6 col-md-3 footer-links">
          <h2>
           Popular artists
          </h2>
          <ul>
           <li>
            <a href="/artist/128962">
             Marty Sampson
            </a>
           </li>
           <li>
            <a href="/artist/4902">
             LaShawn Daniels
            </a>
           </li>
           <li>
            <a href="/artist/20868">
             Deborah Kerr Winans
            </a>
           </li>
           <li>
            <a href="/artist/3668">
             Nikki Sixx
            </a>
           </li>
           <li>
            <a href="/artist/41107">
             Linda Thompson [US]
            </a>
           </li>
           <li>
            <a href="/artist/98705">
             Cindy Cyrus
            </a>
           </li>
           <li>
            <a href="/artist/3187">
             Bob Gaudio
            </a>
           </li>
           <li>
            <a href="/artist/69456">
             Kevin Jonas
            </a>
           </li>
           <li>
            <a href="/artist/112149">
             Christian Ulvaeus
            </a>
           </li>
           <li>
            <a href="/artist/3622">
             John Deacon
            </a>
           </li>
          </ul>
         </section>
        </div>
        <div class="row col-md-12" id="path-closure">
         <ul class="list-inline">
          <li class="list-inline-item">
           <a href="/page/About">
            © 2003-2019
                            secondhandsongs.com
           </a>
          </li>
          <li class="list-inline-item">
           <a href="/page/TermsOfService">
            Terms of Service
           </a>
          </li>
          <li class="list-inline-item">
           <a href="/page/PrivacyPolicy">
            Privacy Policy
           </a>
          </li>
         </ul>
        </div>
       </div>
      </footer>
      <script src="/build/js/app.b87cd868a21dd72b67cb.js">
      </script>
      <script>
       var formToken = null;
      </script>
      <script>
       $(document).ready(function () {
                var $form = $('#root_filter');
    $form.find('.error-field-owner').text('');
    $form.find('.error-field-creator').text('');
    $form.find('.error-field-modifier').text('');
    $form.find('.error-field-adaptationExcluded').text('');
    $form.find('.error-field-christmasExcluded').text('');
    $form.find('.error-field-artistType').text('');
    
            });
      </script>
      <!-- NextMillennium Ads -->
      <script type="text/javascript">
       (function() {var s=document.createElement('script'); s.type='text/javascript'; s.async=true; s.src='//nextmillennium.liqwid.net/?key=D85D-A6F1-B041-B88A'; var x=document.getElementsByTagName('script')[0]; x.parentNode.insertBefore(s,x);})();
      </script>
      <!-- End of NextMillennium Ads -->
      <script>
       highchartsFileName = "/build/js/highcharts.62adb38598e295e56ce3.js";
            $(document).ready(function() {
                var hash = window.location.hash;
                if (hash.indexOf("#_") == 0) {
                    hash = window.location.hash.substring(2);
                    var offset = $("a[name=" + hash + "]").offset();
                    window.scrollTo(offset.left, offset.top-$(window).height()/3);
                }
            });
      </script>
      <script>
       var _gaq = [
                ['_setAccount', 'UA-129438-1'],
                ['_trackPageview']
            ];
            _gaq.push(['_setCustomVar', 1, 'Member Type', 'Visitor', 1]);
            (function (d, t) {
                var g = d.createElement(t), s = d.getElementsByTagName(t)[0];
                g.src = ('https:' == location.protocol ? '//ssl' : '//www') + '.google-analytics.com/ga.js';
                s.parentNode.insertBefore(g, s)
            }(document, 'script'));
      </script>
      <script src="//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US&amp;adInstanceId=bbd8d016-c5be-4bdc-8815-26cf84dfa757">
      </script>
     </body>
    </html>
    


```python
#We would like to extract the <tr> tags belonging to the table, whose id = "vw"
rows = soup.select('#vw tr')
rows
```




    [<tr><th class="field-index "></th>
      <th class="field-release ">Release</th>
      <th class="field-performer ">Performer</th>
      <th class="field-covers text-right">Covers <i class="fa fa-caret-down fa- "></i></th>
      </tr>, <tr>
        <td class="field-index ">1</td>
        <td class="field-release "><a class="link-release" href="/release/712">The Beatles [White Album]</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/41">The Beatles</a></td>
        <td class="field-covers text-right">1634</td>
       </tr>, <tr>
        <td class="field-index ">2</td>
        <td class="field-release "><a class="link-release" href="/release/156">Rubber Soul</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/41">The Beatles</a></td>
        <td class="field-covers text-right">1497</td>
       </tr>, <tr>
        <td class="field-index ">3</td>
        <td class="field-release "><a class="link-release" href="/release/1095">Revolver</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/41">The Beatles</a></td>
        <td class="field-covers text-right">1489</td>
       </tr>, <tr>
        <td class="field-index ">4</td>
        <td class="field-release "><a class="link-release" href="/release/243">Abbey Road</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/41">The Beatles</a></td>
        <td class="field-covers text-right">1468</td>
       </tr>, <tr>
        <td class="field-index ">5</td>
        <td class="field-release "><a class="link-release" href="/release/152911">Meet Me in St. Louis</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/1424+35156">Judy Garland with Georgie Stoll and His Orchestra</a></td>
        <td class="field-covers text-right">1399</td>
       </tr>, <tr>
        <td class="field-index ">6</td>
        <td class="field-release "><a class="link-release" href="/release/133079">Silent Night, Hallowed Night</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/56262">Haydn Quartet</a></td>
        <td class="field-covers text-right">1378</td>
       </tr>, <tr>
        <td class="field-index ">7</td>
        <td class="field-release "><a class="link-release" href="/release/28177">The Christmas Song (Merry Christmas to You)</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/52045">The King Cole Trio with String Choir</a></td>
        <td class="field-covers text-right">1195</td>
       </tr>, <tr>
        <td class="field-index ">8</td>
        <td class="field-release "><a class="link-release" href="/release/31">Sgt. Pepper's Lonely Hearts Club Band</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/41">The Beatles</a></td>
        <td class="field-covers text-right">1107</td>
       </tr>, <tr>
        <td class="field-index ">9</td>
        <td class="field-release "><a class="link-release" href="/release/888">Help!</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/41">The Beatles</a></td>
        <td class="field-covers text-right">1081</td>
       </tr>, <tr>
        <td class="field-index ">10</td>
        <td class="field-release "><a class="link-release" href="/release/18821">Were You Fooling</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/21999">Richard Himber &amp; His Orchestra</a></td>
        <td class="field-covers text-right">996</td>
       </tr>, <tr>
        <td class="field-index ">11</td>
        <td class="field-release "><a class="link-release" href="/release/40215">Jingle Bells</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/56262">Edison Male Quartette</a></td>
        <td class="field-covers text-right">985</td>
       </tr>, <tr>
        <td class="field-index ">12</td>
        <td class="field-release "><a class="link-release" href="/release/74035">Body and Soul</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/33606">Ambrose and His Orchestra</a></td>
        <td class="field-covers text-right">955</td>
       </tr>, <tr>
        <td class="field-index ">13</td>
        <td class="field-release "><a class="link-release" href="/release/83570">God Rest Ye Merry, Gentlemen</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/64422">Meister Glee Singers</a></td>
        <td class="field-covers text-right">901</td>
       </tr>, <tr>
        <td class="field-index ">14</td>
        <td class="field-release "><a class="link-release" href="/release/418">A Hard Day's Night</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/41">The Beatles</a></td>
        <td class="field-covers text-right">891</td>
       </tr>, <tr>
        <td class="field-index ">15</td>
        <td class="field-release "><a class="link-release" href="/release/84167">The First Nowell</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/64817">Tally-Ho!</a></td>
        <td class="field-covers text-right">839</td>
       </tr>, <tr>
        <td class="field-index ">16</td>
        <td class="field-release "><a class="link-release" href="/release/35932">I'll Be Home for Christmas (If Only in My Dreams)</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/243+26334">Bing Crosby with John Scott Trotter and His Orchestra</a></td>
        <td class="field-covers text-right">830</td>
       </tr>, <tr>
        <td class="field-index ">17</td>
        <td class="field-release "><a class="link-release" href="/release/799">The Freewheelin' Bob Dylan</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/158">Bob Dylan</a></td>
        <td class="field-covers text-right">801</td>
       </tr>, <tr>
        <td class="field-index ">18</td>
        <td class="field-release "><a class="link-release" href="/release/83498">Christmas with The Trapp Family Singers</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/64386">The Trapp Family Singers</a></td>
        <td class="field-covers text-right">794</td>
       </tr>, <tr>
        <td class="field-index ">19</td>
        <td class="field-release "><a class="link-release" href="/release/34564">Somebody's Gotta Go</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/6877">Cootie Williams and His Orchestra</a></td>
        <td class="field-covers text-right">738</td>
       </tr>, <tr>
        <td class="field-index ">20</td>
        <td class="field-release "><a class="link-release" href="/release/4363">O Amor o Sorriso e a Flor</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/3058">João Gilberto</a></td>
        <td class="field-covers text-right">715</td>
       </tr>, <tr>
        <td class="field-index ">21</td>
        <td class="field-release "><a class="link-release" href="/release/17479">Let It Snow! Let It Snow! Let It Snow!</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/17403">Vaughn Monroe and His Orchestra</a></td>
        <td class="field-covers text-right">701</td>
       </tr>, <tr>
        <td class="field-index ">22</td>
        <td class="field-release "><a class="link-release" href="/release/4777">Tapestry</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/2270">Carole King</a></td>
        <td class="field-covers text-right">667</td>
       </tr>, <tr>
        <td class="field-index ">23</td>
        <td class="field-release "><a class="link-release" href="/release/40079">One Night in Havana</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/1564">Hoagy Carmichael &amp; His Pals</a></td>
        <td class="field-covers text-right">626</td>
       </tr>, <tr>
        <td class="field-index ">24</td>
        <td class="field-release "><a class="link-release" href="/release/16746">Caravan</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/112830">Barney Bigard and His Jazzopators</a></td>
        <td class="field-covers text-right">620</td>
       </tr>, <tr>
        <td class="field-index ">25</td>
        <td class="field-release "><a class="link-release" href="/release/15333">Moon River</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/233">Henry Mancini, His Orchestra and Chorus</a></td>
        <td class="field-covers text-right">619</td>
       </tr>, <tr>
        <td class="field-index ">26</td>
        <td class="field-release "><a class="link-release" href="/release/64">Bridge over Troubled Water</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/21291">Simon and Garfunkel</a></td>
        <td class="field-covers text-right">606</td>
       </tr>, <tr>
        <td class="field-index ">27</td>
        <td class="field-release "><a class="link-release" href="/release/24142">Hesitating Blues</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/26565">Prince's Band</a></td>
        <td class="field-covers text-right">599</td>
       </tr>, <tr>
        <td class="field-index ">28</td>
        <td class="field-release "><a class="link-release" href="/release/156323">St. Louis Woman - Original Broadway Cast</a></td>
        <td class="field-performer "></td>
        <td class="field-covers text-right">595</td>
       </tr>, <tr>
        <td class="field-index ">29</td>
        <td class="field-release "><a class="link-release" href="/release/4357">Kind of Blue</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/106">Miles Davis</a></td>
        <td class="field-covers text-right">579</td>
       </tr>, <tr>
        <td class="field-index ">30</td>
        <td class="field-release "><a class="link-release" href="/release/39342">Georgia (On My Mind)</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/1564">Hoagy Carmichael and His Orchestra</a></td>
        <td class="field-covers text-right">564</td>
       </tr>, <tr>
        <td class="field-index ">31</td>
        <td class="field-release "><a class="link-release" href="/release/80511">Orfeu Negro - Bande Originale du Film de Marcel Camus</a></td>
        <td class="field-performer "></td>
        <td class="field-covers text-right">562</td>
       </tr>, <tr>
        <td class="field-index ">32</td>
        <td class="field-release "><a class="link-release" href="/release/108">Songs in the Key of Life</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/110">Stevie Wonder</a></td>
        <td class="field-covers text-right">541</td>
       </tr>, <tr>
        <td class="field-index ">33</td>
        <td class="field-release "><a class="link-release" href="/release/35590">Lover Man (Oh, Where Can You Be?)</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/1496">Billie Holiday</a></td>
        <td class="field-covers text-right">539</td>
       </tr>, <tr>
        <td class="field-index ">34</td>
        <td class="field-release "><a class="link-release" href="/release/2545">Giant Steps</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/2281">John Coltrane</a></td>
        <td class="field-covers text-right">533</td>
       </tr>, <tr>
        <td class="field-index ">35</td>
        <td class="field-release "><a class="link-release" href="/release/246700">Love Letters</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/3545">Victor Young and His Concert Orchestra</a></td>
        <td class="field-covers text-right">531</td>
       </tr>, <tr>
        <td class="field-index ">36</td>
        <td class="field-release "><a class="link-release" href="/release/26684">Sleigh Ride</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/5234">Boston Pops Orchestra</a></td>
        <td class="field-covers text-right">529</td>
       </tr>, <tr>
        <td class="field-index ">37</td>
        <td class="field-release "><a class="link-release" href="/release/38878">Willow Weep for Me</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/8159">Ted Fiorito &amp; His Orchestra</a></td>
        <td class="field-covers text-right">527</td>
       </tr>, <tr>
        <td class="field-index ">38</td>
        <td class="field-release "><a class="link-release" href="/release/760">Imagine</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/143">John Lennon</a></td>
        <td class="field-covers text-right">526</td>
       </tr>, <tr>
        <td class="field-index ">39</td>
        <td class="field-release "><a class="link-release" href="/release/40506">Rudolph, the Red-Nosed Reindeer</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/8191+137584">Gene Autry and The Pinafores with Orchestral Accompaniment</a></td>
        <td class="field-covers text-right">524</td>
       </tr>, <tr>
        <td class="field-index ">40</td>
        <td class="field-release "><a class="link-release" href="/release/25533">Harlem on Parade</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/12006">Gene Krupa &amp; His Orchestra</a></td>
        <td class="field-covers text-right">511</td>
       </tr>, <tr>
        <td class="field-index ">41</td>
        <td class="field-release "><a class="link-release" href="/release/72925">Fools Rush In</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/11273">Chick Bullock &amp; His Orchestra</a></td>
        <td class="field-covers text-right">510</td>
       </tr>, <tr>
        <td class="field-index ">42</td>
        <td class="field-release "><a class="link-release" href="/release/32899">A Fine Romance</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/11997">Guy Lombardo and His Royal Canadians</a></td>
        <td class="field-covers text-right">500</td>
       </tr>, <tr>
        <td class="field-index ">43</td>
        <td class="field-release "><a class="link-release" href="/release/26980">Yearning Just for You</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/19876">Ben Bernie and His Hotel Roosevelt Orchestra</a></td>
        <td class="field-covers text-right">499</td>
       </tr>, <tr>
        <td class="field-index ">44</td>
        <td class="field-release "><a class="link-release" href="/release/2124">Blue</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/5191">Joni Mitchell</a></td>
        <td class="field-covers text-right">493</td>
       </tr>, <tr>
        <td class="field-index ">45</td>
        <td class="field-release "><a class="link-release" href="/release/40077">In a Sentimental Mood</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/4305">Duke Ellington and His Orchestra</a></td>
        <td class="field-covers text-right">488</td>
       </tr>, <tr>
        <td class="field-index ">46</td>
        <td class="field-release "><a class="link-release" href="/release/52700">Love Is Here to Stay</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/17024">Ella Logan</a></td>
        <td class="field-covers text-right">486</td>
       </tr>, <tr>
        <td class="field-index ">47</td>
        <td class="field-release "><a class="link-release" href="/release/115680">A Shine on Your Shoes</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/11277">Leo Reisman and His Orchestra</a></td>
        <td class="field-covers text-right">483</td>
       </tr>, <tr>
        <td class="field-index ">48</td>
        <td class="field-release "><a class="link-release" href="/release/94835">Don't Do Something to Someone Else (That You Wouldn't Want Done to You)</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/6842">Gordon Jenkins and His Orchestra</a></td>
        <td class="field-covers text-right">482</td>
       </tr>, <tr>
        <td class="field-index ">49</td>
        <td class="field-release "><a class="link-release" href="/release/18593">A Charlie Brown Christmas</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/14385">Vince Guaraldi</a></td>
        <td class="field-covers text-right">478</td>
       </tr>, <tr>
        <td class="field-index ">50</td>
        <td class="field-release "><a class="link-release" href="/release/3295">The Sandpiper - Original Motion Picture Soundtrack</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/3001">Johnny Mandel</a></td>
        <td class="field-covers text-right">476</td>
       </tr>, <tr>
        <td class="field-index ">51</td>
        <td class="field-release "><a class="link-release" href="/release/3005">Talking Book</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/110">Stevie Wonder</a></td>
        <td class="field-covers text-right">476</td>
       </tr>, <tr>
        <td class="field-index ">52</td>
        <td class="field-release "><a class="link-release" href="/release/273">Thriller</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/254">Michael Jackson</a></td>
        <td class="field-covers text-right">475</td>
       </tr>, <tr>
        <td class="field-index ">53</td>
        <td class="field-release "><a class="link-release" href="/release/38812">What a Wonderful World</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/2823">Louis Armstrong</a></td>
        <td class="field-covers text-right">473</td>
       </tr>, <tr>
        <td class="field-index ">54</td>
        <td class="field-release "><a class="link-release" href="/release/18899">Blue Christmas</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/22034">Doye O'Dell</a></td>
        <td class="field-covers text-right">466</td>
       </tr>, <tr>
        <td class="field-index ">55</td>
        <td class="field-release "><a class="link-release" href="/release/104207">Poor Hawthorne</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/77226">Ukrainian National Chorus</a></td>
        <td class="field-covers text-right">466</td>
       </tr>, <tr>
        <td class="field-index ">56</td>
        <td class="field-release "><a class="link-release" href="/release/28175">Nature Boy</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/320">King Cole</a></td>
        <td class="field-covers text-right">463</td>
       </tr>, <tr>
        <td class="field-index ">57</td>
        <td class="field-release "><a class="link-release" href="/release/20965">I'll Follow You</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/6053+29799">Paul Whiteman and His Orchestra with vocal refrain by Red McKenzie</a></td>
        <td class="field-covers text-right">463</td>
       </tr>, <tr>
        <td class="field-index ">58</td>
        <td class="field-release "><a class="link-release" href="/release/10964">Thelonious</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/2288">Thelonious Monk Trio</a></td>
        <td class="field-covers text-right">461</td>
       </tr>, <tr>
        <td class="field-index ">59</td>
        <td class="field-release "><a class="link-release" href="/release/7287">West Side Story [OBC]</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/9531+41391+113126+113782">Leonard Bernstein with Irwin Kostal and Sid Ramin – Original Broadway Cast</a></td>
        <td class="field-covers text-right">458</td>
       </tr>, <tr>
        <td class="field-index ">60</td>
        <td class="field-release "><a class="link-release" href="/release/9274">Equinox</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/500">Sergio Mendes &amp; Brasil '66</a></td>
        <td class="field-covers text-right">457</td>
       </tr>, <tr>
        <td class="field-index ">61</td>
        <td class="field-release "><a class="link-release" href="/release/98188">Misty</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/2481">Erroll Garner Trio</a></td>
        <td class="field-covers text-right">456</td>
       </tr>, <tr>
        <td class="field-index ">62</td>
        <td class="field-release "><a class="link-release" href="/release/32376">Cry Me a River</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/1246">Julie London</a></td>
        <td class="field-covers text-right">449</td>
       </tr>, <tr>
        <td class="field-index ">63</td>
        <td class="field-release "><a class="link-release" href="/release/2407">Nevermind</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/169">Nirvana [US]</a></td>
        <td class="field-covers text-right">447</td>
       </tr>, <tr>
        <td class="field-index ">64</td>
        <td class="field-release "><a class="link-release" href="/release/112">Blue Hawaii</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/103">Elvis Presley</a></td>
        <td class="field-covers text-right">442</td>
       </tr>, <tr>
        <td class="field-index ">65</td>
        <td class="field-release "><a class="link-release" href="/release/12842">Hey Jude</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/41">The Beatles</a></td>
        <td class="field-covers text-right">442</td>
       </tr>, <tr>
        <td class="field-index ">66</td>
        <td class="field-release "><a class="link-release" href="/release/16739">Turn on the Heat</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/20506">Bert Stock and His Orchestra</a></td>
        <td class="field-covers text-right">440</td>
       </tr>, <tr>
        <td class="field-index ">67</td>
        <td class="field-release "><a class="link-release" href="/release/69028">Fever</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/8029">Little Willie John</a></td>
        <td class="field-covers text-right">434</td>
       </tr>, <tr>
        <td class="field-index ">68</td>
        <td class="field-release "><a class="link-release" href="/release/140562">"Tryout" - A Series of Private Rehearsal Recordings</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/3278+4029">Kurt Weill and Ira Gershwin</a></td>
        <td class="field-covers text-right">434</td>
       </tr>, <tr>
        <td class="field-index ">69</td>
        <td class="field-release "><a class="link-release" href="/release/100765">They Can't Take That Away from Me</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/2232+11247">Fred Astaire with Johnny Green and His Orchestra</a></td>
        <td class="field-covers text-right">434</td>
       </tr>, <tr>
        <td class="field-index ">70</td>
        <td class="field-release "><a class="link-release" href="/release/101382">True</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/75527">Al Bowlly</a></td>
        <td class="field-covers text-right">430</td>
       </tr>, <tr>
        <td class="field-index ">71</td>
        <td class="field-release "><a class="link-release" href="/release/85842">Angel Eyes</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/45892">Herb Jeffries</a></td>
        <td class="field-covers text-right">427</td>
       </tr>, <tr>
        <td class="field-index ">72</td>
        <td class="field-release "><a class="link-release" href="/release/89906">Merry-Go-Round</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/4305">Duke Ellington and His Orchestra</a></td>
        <td class="field-covers text-right">426</td>
       </tr>, <tr>
        <td class="field-index ">73</td>
        <td class="field-release "><a class="link-release" href="/release/3211">The Sound of Music</a></td>
        <td class="field-performer "></td>
        <td class="field-covers text-right">423</td>
       </tr>, <tr>
        <td class="field-index ">74</td>
        <td class="field-release "><a class="link-release" href="/release/18534">Never No Lament</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/4305">Duke Ellington and His Famous Orchestra</a></td>
        <td class="field-covers text-right">418</td>
       </tr>, <tr>
        <td class="field-index ">75</td>
        <td class="field-release "><a class="link-release" href="/release/13461">Oh Lonesome Me</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/1415">Don Gibson</a></td>
        <td class="field-covers text-right">418</td>
       </tr>, <tr>
        <td class="field-index ">76</td>
        <td class="field-release "><a class="link-release" href="/release/21013">Take the "A" Train</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/4305">Duke Ellington and His Famous Orchestra</a></td>
        <td class="field-covers text-right">416</td>
       </tr>, <tr>
        <td class="field-index ">77</td>
        <td class="field-release "><a class="link-release" href="/release/1483">Wildflowers</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/1421">Judy Collins</a></td>
        <td class="field-covers text-right">412</td>
       </tr>, <tr>
        <td class="field-index ">78</td>
        <td class="field-release "><a class="link-release" href="/release/704">Various Positions</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/150">Leonard Cohen</a></td>
        <td class="field-covers text-right">410</td>
       </tr>, <tr>
        <td class="field-index ">79</td>
        <td class="field-release "><a class="link-release" href="/release/27100">You Go to My Head</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/7542">Larry Clinton &amp; His Orchestra</a></td>
        <td class="field-covers text-right">409</td>
       </tr>, <tr>
        <td class="field-index ">80</td>
        <td class="field-release "><a class="link-release" href="/release/162807">Music from Beyond the Moon</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/11874+15990">Vic Damone and Music by Camarata</a></td>
        <td class="field-covers text-right">405</td>
       </tr>, <tr>
        <td class="field-index ">81</td>
        <td class="field-release "><a class="link-release" href="/release/153502">When You Wish Upon a Star - I've Got No Strings</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/3545+3589+12173">Cliff Edwards with Victor Young and His Orchestra and The Ken Darby Singers</a></td>
        <td class="field-covers text-right">398</td>
       </tr>, <tr>
        <td class="field-index ">82</td>
        <td class="field-release "><a class="link-release" href="/release/3170">The Wall</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/560">Pink Floyd</a></td>
        <td class="field-covers text-right">398</td>
       </tr>, <tr>
        <td class="field-index ">83</td>
        <td class="field-release "><a class="link-release" href="/release/97105">You'd Be So Nice to Come Home To</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/11275">Dick Jurgens and His Orchestra</a></td>
        <td class="field-covers text-right">394</td>
       </tr>, <tr>
        <td class="field-index ">84</td>
        <td class="field-release "><a class="link-release" href="/release/21374">What the World Needs Now - Stan Getz Plays Bacharach and David</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/2205">Stan Getz</a></td>
        <td class="field-covers text-right">391</td>
       </tr>, <tr>
        <td class="field-index ">85</td>
        <td class="field-release "><a class="link-release" href="/release/31927">New Britain</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/33303">The Original Sacred Harp Choir</a></td>
        <td class="field-covers text-right">387</td>
       </tr>, <tr>
        <td class="field-index ">86</td>
        <td class="field-release "><a class="link-release" href="/release/2467">The Bootleg Series Volumes 1-3</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/158">Bob Dylan</a></td>
        <td class="field-covers text-right">386</td>
       </tr>, <tr>
        <td class="field-index ">87</td>
        <td class="field-release "><a class="link-release" href="/release/17987">God Bless the Child</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/1496">Billie Holiday</a></td>
        <td class="field-covers text-right">385</td>
       </tr>, <tr>
        <td class="field-index ">88</td>
        <td class="field-release "><a class="link-release" href="/release/38917">Don't Blame Me</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/979+3251">Sarah Vaughan with George Treadwell's Orchestra</a></td>
        <td class="field-covers text-right">381</td>
       </tr>, <tr>
        <td class="field-index ">89</td>
        <td class="field-release "><a class="link-release" href="/release/4642">The Joshua Tree</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/297">U2</a></td>
        <td class="field-covers text-right">379</td>
       </tr>, <tr>
        <td class="field-index ">90</td>
        <td class="field-release "><a class="link-release" href="/release/2749">Comme d'habitude</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/2077">Claude François</a></td>
        <td class="field-covers text-right">379</td>
       </tr>, <tr>
        <td class="field-index ">91</td>
        <td class="field-release "><a class="link-release" href="/release/20932">Carnegie Hall, November 13, 1948</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/4305">Duke Ellington and His Orchestra</a></td>
        <td class="field-covers text-right">378</td>
       </tr>, <tr>
        <td class="field-index ">92</td>
        <td class="field-release "><a class="link-release" href="/release/83778">Bye Bye Blackbird</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/19880">Sam Lanin's Dance Orchestra</a></td>
        <td class="field-covers text-right">377</td>
       </tr>, <tr>
        <td class="field-index ">93</td>
        <td class="field-release "><a class="link-release" href="/release/1985">Innervisions</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/110">Stevie Wonder</a></td>
        <td class="field-covers text-right">377</td>
       </tr>, <tr>
        <td class="field-index ">94</td>
        <td class="field-release "><a class="link-release" href="/release/295">Bringing It All Back Home</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/158">Bob Dylan</a></td>
        <td class="field-covers text-right">376</td>
       </tr>, <tr>
        <td class="field-index ">95</td>
        <td class="field-release "><a class="link-release" href="/release/96450">Secret Love</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/401">Doris Day</a></td>
        <td class="field-covers text-right">375</td>
       </tr>, <tr>
        <td class="field-index ">96</td>
        <td class="field-release "><a class="link-release" href="/release/25790">After You've Gone</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/19977+22089">Henry Burr &amp; Albert Campbell</a></td>
        <td class="field-covers text-right">374</td>
       </tr>, <tr>
        <td class="field-index ">97</td>
        <td class="field-release "><a class="link-release" href="/release/3143">Saturday Night Fever</a></td>
        <td class="field-performer "></td>
        <td class="field-covers text-right">369</td>
       </tr>, <tr>
        <td class="field-index ">98</td>
        <td class="field-release "><a class="link-release" href="/release/317">Blonde on Blonde</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/158">Bob Dylan</a></td>
        <td class="field-covers text-right">368</td>
       </tr>, <tr>
        <td class="field-index ">99</td>
        <td class="field-release "><a class="link-release" href="/release/12838">Let It Be</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/41">The Beatles</a></td>
        <td class="field-covers text-right">368</td>
       </tr>, <tr>
        <td class="field-index ">100</td>
        <td class="field-release "><a class="link-release" href="/release/71704">Dreamy Blues</a></td>
        <td class="field-performer "><a class="link-performer" href="/artist/4305">The Jungle Band</a></td>
        <td class="field-covers text-right">368</td>
       </tr>]




```python
frame = []
for row in rows:
    frame.append([td.text for td in row.select('td')])
    print([td.text for td in row.select('td')])
```

    []
    ['1', 'The Beatles [White Album]', 'The Beatles', '1634']
    ['2', 'Rubber Soul', 'The Beatles', '1497']
    ['3', 'Revolver', 'The Beatles', '1489']
    ['4', 'Abbey Road', 'The Beatles', '1468']
    ['5', 'Meet Me in St. Louis', 'Judy Garland with Georgie Stoll and His Orchestra', '1399']
    ['6', 'Silent Night, Hallowed Night', 'Haydn Quartet', '1378']
    ['7', 'The Christmas Song (Merry Christmas to You)', 'The King Cole Trio with String Choir', '1195']
    ['8', "Sgt. Pepper's Lonely Hearts Club Band", 'The Beatles', '1107']
    ['9', 'Help!', 'The Beatles', '1081']
    ['10', 'Were You Fooling', 'Richard Himber & His Orchestra', '996']
    ['11', 'Jingle Bells', 'Edison Male Quartette', '985']
    ['12', 'Body and Soul', 'Ambrose and His Orchestra', '955']
    ['13', 'God Rest Ye Merry, Gentlemen', 'Meister Glee Singers', '901']
    ['14', "A Hard Day's Night", 'The Beatles', '891']
    ['15', 'The First Nowell', 'Tally-Ho!', '839']
    ['16', "I'll Be Home for Christmas (If Only in My Dreams)", 'Bing Crosby with John Scott Trotter and His Orchestra', '830']
    ['17', "The Freewheelin' Bob Dylan", 'Bob Dylan', '801']
    ['18', 'Christmas with The Trapp Family Singers', 'The Trapp Family Singers', '794']
    ['19', "Somebody's Gotta Go", 'Cootie Williams and His Orchestra', '738']
    ['20', 'O Amor o Sorriso e a Flor', 'João Gilberto', '715']
    ['21', 'Let It Snow! Let It Snow! Let It Snow!', 'Vaughn Monroe and His Orchestra', '701']
    ['22', 'Tapestry', 'Carole King', '667']
    ['23', 'One Night in Havana', 'Hoagy Carmichael & His Pals', '626']
    ['24', 'Caravan', 'Barney Bigard and His Jazzopators', '620']
    ['25', 'Moon River', 'Henry Mancini, His Orchestra and Chorus', '619']
    ['26', 'Bridge over Troubled Water', 'Simon and Garfunkel', '606']
    ['27', 'Hesitating Blues', "Prince's Band", '599']
    ['28', 'St. Louis Woman - Original Broadway Cast', '', '595']
    ['29', 'Kind of Blue', 'Miles Davis', '579']
    ['30', 'Georgia (On My Mind)', 'Hoagy Carmichael and His Orchestra', '564']
    ['31', 'Orfeu Negro - Bande Originale du Film de Marcel Camus', '', '562']
    ['32', 'Songs in the Key of Life', 'Stevie Wonder', '541']
    ['33', 'Lover Man (Oh, Where Can You Be?)', 'Billie Holiday', '539']
    ['34', 'Giant Steps', 'John Coltrane', '533']
    ['35', 'Love Letters', 'Victor Young and His Concert Orchestra', '531']
    ['36', 'Sleigh Ride', 'Boston Pops Orchestra', '529']
    ['37', 'Willow Weep for Me', 'Ted Fiorito & His Orchestra', '527']
    ['38', 'Imagine', 'John Lennon', '526']
    ['39', 'Rudolph, the Red-Nosed Reindeer', 'Gene Autry and The Pinafores with Orchestral Accompaniment', '524']
    ['40', 'Harlem on Parade', 'Gene Krupa & His Orchestra', '511']
    ['41', 'Fools Rush In', 'Chick Bullock & His Orchestra', '510']
    ['42', 'A Fine Romance', 'Guy Lombardo and His Royal Canadians', '500']
    ['43', 'Yearning Just for You', 'Ben Bernie and His Hotel Roosevelt Orchestra', '499']
    ['44', 'Blue', 'Joni Mitchell', '493']
    ['45', 'In a Sentimental Mood', 'Duke Ellington and His Orchestra', '488']
    ['46', 'Love Is Here to Stay', 'Ella Logan', '486']
    ['47', 'A Shine on Your Shoes', 'Leo Reisman and His Orchestra', '483']
    ['48', "Don't Do Something to Someone Else (That You Wouldn't Want Done to You)", 'Gordon Jenkins and His Orchestra', '482']
    ['49', 'A Charlie Brown Christmas', 'Vince Guaraldi', '478']
    ['50', 'The Sandpiper - Original Motion Picture Soundtrack', 'Johnny Mandel', '476']
    ['51', 'Talking Book', 'Stevie Wonder', '476']
    ['52', 'Thriller', 'Michael Jackson', '475']
    ['53', 'What a Wonderful World', 'Louis Armstrong', '473']
    ['54', 'Blue Christmas', "Doye O'Dell", '466']
    ['55', 'Poor Hawthorne', 'Ukrainian National Chorus', '466']
    ['56', 'Nature Boy', 'King Cole', '463']
    ['57', "I'll Follow You", 'Paul Whiteman and His Orchestra with vocal refrain by Red McKenzie', '463']
    ['58', 'Thelonious', 'Thelonious Monk Trio', '461']
    ['59', 'West Side Story [OBC]', 'Leonard Bernstein with Irwin Kostal and Sid Ramin – Original Broadway Cast', '458']
    ['60', 'Equinox', "Sergio Mendes & Brasil '66", '457']
    ['61', 'Misty', 'Erroll Garner Trio', '456']
    ['62', 'Cry Me a River', 'Julie London', '449']
    ['63', 'Nevermind', 'Nirvana [US]', '447']
    ['64', 'Blue Hawaii', 'Elvis Presley', '442']
    ['65', 'Hey Jude', 'The Beatles', '442']
    ['66', 'Turn on the Heat', 'Bert Stock and His Orchestra', '440']
    ['67', 'Fever', 'Little Willie John', '434']
    ['68', '"Tryout" - A Series of Private Rehearsal Recordings', 'Kurt Weill and Ira Gershwin', '434']
    ['69', "They Can't Take That Away from Me", 'Fred Astaire with Johnny Green and His Orchestra', '434']
    ['70', 'True', 'Al Bowlly', '430']
    ['71', 'Angel Eyes', 'Herb Jeffries', '427']
    ['72', 'Merry-Go-Round', 'Duke Ellington and His Orchestra', '426']
    ['73', 'The Sound of Music', '', '423']
    ['74', 'Never No Lament', 'Duke Ellington and His Famous Orchestra', '418']
    ['75', 'Oh Lonesome Me', 'Don Gibson', '418']
    ['76', 'Take the "A" Train', 'Duke Ellington and His Famous Orchestra', '416']
    ['77', 'Wildflowers', 'Judy Collins', '412']
    ['78', 'Various Positions', 'Leonard Cohen', '410']
    ['79', 'You Go to My Head', 'Larry Clinton & His Orchestra', '409']
    ['80', 'Music from Beyond the Moon', 'Vic Damone and Music by Camarata', '405']
    ['81', "When You Wish Upon a Star - I've Got No Strings", 'Cliff Edwards with Victor Young and His Orchestra and The Ken Darby Singers', '398']
    ['82', 'The Wall', 'Pink Floyd', '398']
    ['83', "You'd Be So Nice to Come Home To", 'Dick Jurgens and His Orchestra', '394']
    ['84', 'What the World Needs Now - Stan Getz Plays Bacharach and David', 'Stan Getz', '391']
    ['85', 'New Britain', 'The Original Sacred Harp Choir', '387']
    ['86', 'The Bootleg Series Volumes 1-3', 'Bob Dylan', '386']
    ['87', 'God Bless the Child', 'Billie Holiday', '385']
    ['88', "Don't Blame Me", "Sarah Vaughan with George Treadwell's Orchestra", '381']
    ['89', 'The Joshua Tree', 'U2', '379']
    ['90', "Comme d'habitude", 'Claude François', '379']
    ['91', 'Carnegie Hall, November 13, 1948', 'Duke Ellington and His Orchestra', '378']
    ['92', 'Bye Bye Blackbird', "Sam Lanin's Dance Orchestra", '377']
    ['93', 'Innervisions', 'Stevie Wonder', '377']
    ['94', 'Bringing It All Back Home', 'Bob Dylan', '376']
    ['95', 'Secret Love', 'Doris Day', '375']
    ['96', "After You've Gone", 'Henry Burr & Albert Campbell', '374']
    ['97', 'Saturday Night Fever', '', '369']
    ['98', 'Blonde on Blonde', 'Bob Dylan', '368']
    ['99', 'Let It Be', 'The Beatles', '368']
    ['100', 'Dreamy Blues', 'The Jungle Band', '368']
    

## Another way we could've approached this scenario would be to use Pandas, which may have been easier. However, I'd prefer to use BeautifulSoup for purposes of this example.


```python
#table = pd.read_html('https://secondhandsongs.com/statistics?sort=covers&list=stats_release_covers')[0]
#print(table)
```


```python
df = pd.DataFrame(frame)
df.columns = ['Rank', 'Album', 'Artist', 'Count']
df.reset_index()
df.drop(0, inplace=True)
#Remove the zero index. Now everything is ranked 1-100
```


```python
df.tail(20)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Album</th>
      <th>Artist</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>81</th>
      <td>81</td>
      <td>When You Wish Upon a Star - I've Got No Strings</td>
      <td>Cliff Edwards with Victor Young and His Orches...</td>
      <td>398</td>
    </tr>
    <tr>
      <th>82</th>
      <td>82</td>
      <td>The Wall</td>
      <td>Pink Floyd</td>
      <td>398</td>
    </tr>
    <tr>
      <th>83</th>
      <td>83</td>
      <td>You'd Be So Nice to Come Home To</td>
      <td>Dick Jurgens and His Orchestra</td>
      <td>394</td>
    </tr>
    <tr>
      <th>84</th>
      <td>84</td>
      <td>What the World Needs Now - Stan Getz Plays Bac...</td>
      <td>Stan Getz</td>
      <td>391</td>
    </tr>
    <tr>
      <th>85</th>
      <td>85</td>
      <td>New Britain</td>
      <td>The Original Sacred Harp Choir</td>
      <td>387</td>
    </tr>
    <tr>
      <th>86</th>
      <td>86</td>
      <td>The Bootleg Series Volumes 1-3</td>
      <td>Bob Dylan</td>
      <td>386</td>
    </tr>
    <tr>
      <th>87</th>
      <td>87</td>
      <td>God Bless the Child</td>
      <td>Billie Holiday</td>
      <td>385</td>
    </tr>
    <tr>
      <th>88</th>
      <td>88</td>
      <td>Don't Blame Me</td>
      <td>Sarah Vaughan with George Treadwell's Orchestra</td>
      <td>381</td>
    </tr>
    <tr>
      <th>89</th>
      <td>89</td>
      <td>The Joshua Tree</td>
      <td>U2</td>
      <td>379</td>
    </tr>
    <tr>
      <th>90</th>
      <td>90</td>
      <td>Comme d'habitude</td>
      <td>Claude François</td>
      <td>379</td>
    </tr>
    <tr>
      <th>91</th>
      <td>91</td>
      <td>Carnegie Hall, November 13, 1948</td>
      <td>Duke Ellington and His Orchestra</td>
      <td>378</td>
    </tr>
    <tr>
      <th>92</th>
      <td>92</td>
      <td>Bye Bye Blackbird</td>
      <td>Sam Lanin's Dance Orchestra</td>
      <td>377</td>
    </tr>
    <tr>
      <th>93</th>
      <td>93</td>
      <td>Innervisions</td>
      <td>Stevie Wonder</td>
      <td>377</td>
    </tr>
    <tr>
      <th>94</th>
      <td>94</td>
      <td>Bringing It All Back Home</td>
      <td>Bob Dylan</td>
      <td>376</td>
    </tr>
    <tr>
      <th>95</th>
      <td>95</td>
      <td>Secret Love</td>
      <td>Doris Day</td>
      <td>375</td>
    </tr>
    <tr>
      <th>96</th>
      <td>96</td>
      <td>After You've Gone</td>
      <td>Henry Burr &amp; Albert Campbell</td>
      <td>374</td>
    </tr>
    <tr>
      <th>97</th>
      <td>97</td>
      <td>Saturday Night Fever</td>
      <td></td>
      <td>369</td>
    </tr>
    <tr>
      <th>98</th>
      <td>98</td>
      <td>Blonde on Blonde</td>
      <td>Bob Dylan</td>
      <td>368</td>
    </tr>
    <tr>
      <th>99</th>
      <td>99</td>
      <td>Let It Be</td>
      <td>The Beatles</td>
      <td>368</td>
    </tr>
    <tr>
      <th>100</th>
      <td>100</td>
      <td>Dreamy Blues</td>
      <td>The Jungle Band</td>
      <td>368</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Create a copy of our DataFrame for some Data Visualization.
df1 = df[0:9]
df1 = df1.astype({'Count':int,'Rank':int}) #Converting the columns to be numeric, in order to be used for Plotting.
```

## We will use the Seaborn library (my favorite for Data Visualization), to create a graph to analyze the data more easily. This graph represents the top 10 covered Albums and their respective counts. We can clearly tell that for some reason, 6 of the 10 most covered records belong to The Beatles! 


```python
sns.barplot(x= "Count",y="Album",data=df1)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1a948ccceb8>




![png](output_13_1.png)



```python
df['Count'] = df['Count'].astype(int)
```


```python
df['Count'].sum()
```




    58925




```python
#The total Count of covers belonging to a Beatles Album:
Beatle = df.loc[df['Artist'] == 'The Beatles', 'Count'].sum()
Beatle
```




    9977




```python
#The total Count of covers not belonging to a Beatles Album:
Not_beatle = Beatle = df.loc[df['Artist'] != 'The Beatles', 'Count'].sum()
Not_beatle
```




    48948




```python
labels = ['Beatles', 'Non-Beatles']
sizes = [9977,48948]
colors = ['gold', 'yellowgreen']
explode = [0.1, 0]
```

## Using a simple Pie chart, we can see that the Beatles hold roughly 1/6 of the total number of Covers, in addition to holding the top 4 ranks. People clearly love this band!


```python
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', colors = ['#66b3ff', '#99ff99'],
        shadow=True, startangle=90)
plt.tight_layout()
plt.axis('equal')  
plt.show()
```


![png](output_20_0.png)


# This is the end of this project. We've conducted WebScraping & Data Manipulation/Visualization using various Python modules (BeautifulSoup, Numpy, Pandas, and Seaborn). Thanks for stopping by and please feel free to visit my Data Science blog: helloworldofdata.webnode.com
