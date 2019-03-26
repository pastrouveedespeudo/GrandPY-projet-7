
<!DOCTYPE html>
    <html>
        <head>
                     
            <meta charset="utf-8"/>
            <title>GrandPY</title>
    
            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>

            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
            <link href="/static/styles/css/default.css" rel="stylesheet" type="text/css"/>

            <script async defer
                    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCt2O8fe5cHDLkjjFk4TQ9Os5Y3vFGmqU8&callback=initMap">
            </script>

            
            <div class="container col-lg-11">
               <div class="row">

                    <div class="col-lg-1 col-xs-1">
                        <img src="static/images/image1.jpg" id="logo" alt="logo"/>
                    </div>

                    <div class="col-lg-11 col-xs-10" id="titres">
                      <h1>HOME</h1>
                      <h2>Hey I'm GrandCat</h2>
                      <center><h3>Site exclusivement réservé à la recherche d'adresse</h3></center>
                   </div>
                  
              </div>
          </div>

        </head>


        <body>
          {% block body %}{% endblock body %}
        </body>
          
    </html>









