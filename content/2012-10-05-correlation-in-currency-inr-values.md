Title: Correlation between INR values of different currencies
date: 2012-10-05 11:16
Tags: data, clojure

<article comments="1">
  <title>Correlation between INR values of different currencies</title>
  <date>2012-09-05 11:31</date>
  <tags>
    <tag>data</tag>
    <tag>clojure</tag>
  </tags>
</article>

<summary>
  <p>
  This is an interesting take away example from the class
   which <a href="http://www.s-anand.net/">Anand</a> is teaching at
   NIAS.
Here we are trying to correlate between the INR values of various
   currencies like AUD, CNY (Chinese Yen), EUR, GBP (Great Britain
   Pound), JPY, SGD, USD and find the positive or negative
   correlations. The focus is on data collection and transformation. 
  </p>
</summary>

<section>
  <p>
    The first part is the identification of a proper source to get the
    data. <a href="http://www.oanda.com">oanda.com</a> is one such source
    from which historic currency exchange rates can be obtained.
  </p>
  <p>
    The next part is the development of an automated/easy way of obtaining
    the data from the site, suitable for transformation. With some
    help from develpment tools in the browser the url of the
    download link can be found.
    It looks something like
    <br/>
      
    
    <script src="https://gist.github.com/3638650.js?file=data2_url.sh"></script>
    <br/>
    Here we can find that SGD is the currency that is being used, with
    little exprimentation it can be found that we can download data
    for other currencies by altering this URL (example - replace SGD
    with JPY for downloading data for Japanese yen)
  </P>
  <p>
    The next is the transformation part, the downloaded csv files
    contains data that are not required for further analysis that
    should be filtered to get the required data. In this case we have
    to filter the first 5 lines, that is done by using <code>tail -n +6</code>,
    which prints starting from the 6th line and we have to also filter
    the last 4 lines and this is done by using <code> head -n -4</code>, which
    prints all lines but the last 4 lines.
  </p>
  <p>
    We also combine the data and make a single csv file containing data of all currencies
    for easy consumption, this can be done using
  <p>
    <code>
    paste AUD.csv CNY.csv EUR.csv GBP.csv JPY.csv SGD.csv USD.csv |sed
    's/\t/,/g'>alldata.csv
    </code>
  </p>
  <p>
    The complete code for the steps so far
    <br/>
    <code>
      <script src="https://gist.github.com/3638103.js?file=gistfile1.sh"></script>
    </code>
  </P>
  <p>
    The next step is the visualization, The choice of tools for
    visualization is left open, I prefer clojure with incanter.
    Here is the clojure snippet
  </p>
  <p>
    load the data  
    <code>
     <script src="https://gist.github.com/3638130.js?file=data2_currency_read_data.clj"></script>
    </code>
    plot it
    <code>
     <script src="https://gist.github.com/3638148.js?file=blog_data2_unnormalized_plot.clj"></script>
    </code>
  </p>
  <p>
    Here is how it looks - 
    <br/>
    <a href="http://www.flickr.com/photos/86708945@N08/7937082534/"
    title="data2_currency_correlation_notnormalized by tutysara, on
    Flickr"><img src="http://farm9.staticflickr.com/8299/7937082534_5b636f6671.jpg"
    width="500" height="400"
    alt="data2_currency_correlation_notnormalized"></a>
  </p>
  <p>
    It can be found that it is difficult to compare data on different
    scales, normalization helps us in this case (data-mean/mean)
    <br/>
    Here is a function to normalize data
  <p>
    <script src="https://gist.github.com/3638406.js?file=data2_currency_normalize_data.clj"></script>
  </P>
  <p>
    and the plot is updated to show the normalized data
    <code>
    <script src="https://gist.github.com/3638436.js?file=data2_currency_normalize_plot.clj"></script>
    </code>
  </P>
  <p>
    Here is how it looks
    <br/>
    <a href="http://www.flickr.com/photos/86708945@N08/7937082716/"
    title="data2_currency_correlation_normalized by tutysara, on
    Flickr"><img src="http://farm9.staticflickr.com/8446/7937082716_e8134a87d4.jpg"
    width="500" height="353"
    alt="data2_currency_correlation_normalized"></a>
  </p>
  <p>
    the complete code
    <code>
<script src="https://gist.github.com/3638556.js?file=blog_data2_complete_code.clj"></script>
    </code>
  </p>
 <section>
