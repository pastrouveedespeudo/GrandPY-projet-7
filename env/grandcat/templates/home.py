{%extends "core/default.html"%}

{% block body %}

            <h5 class="mb-5" id="p" style="font-size:2.5vw;">Entrez une addresse ! on la cherche pour vous, allez donc essayer note tchat !</h5>



              <div class="container col-xs-12 col-sm-12 col-md-12 col-lg-12">
                  <div class="row">
               
                      <div id="map" class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
                        <img src="/static/images/yo.jpg" id="payschat"/>
            
                        <img src="/static/images/p.jpg" id="payschat"/>
                      </div>
               
                  </div>
              </div>

            <br>

             <div class="container col-xs-12 col-sm-12 col-md-12 col-lg-12">
                 <div class="row">

                      <div id="monCadre" class="col-xs-offset-3 col-sm-offset-0 col-md-offset-0 col-lg-5"></div>
                      <div class="col-xs-0 hidden-sm hidden-md col-lg-1"><br></div>
                      <div id="monCadreWiki" class="col-xs-offset-3 col-sm-offset-0 col-md-offset-0 col-lg-6"></div>           
                </div>
            </div>



            <br>
            <form id="form_data">
                <div class="container col-xs-12 col-sm-12 col-md-12 col-lg-12 style="text-align:center;" id="ud">
                    <div class="row">
                    
                        
                        <input type="text" style="width:84%; text-align:center; border-radius:10px; border:2px solid black; height:50px;
                        font-size: 1.5vw;" id="idRecupInfo"
                            placeholder="Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"/><br>
          
                        <input type="submit" id="sub" value="Enter" id="idButtonInput"
                            style="width:15%; border:2px solid black; height:50px; border-radius:10px; font-size: 1.5vw;"/>
                       
 
                   </div>
                </div>
             </form>

            <div id="monCadreHidden" style="display:none"></div>
            <div id="monCadreHidden2" style="display:none"></div>

                      
                 
        </div>
    </div>
            <a href ="/tchat" style="font-size:1.5vw; color:black;">
                Viens donc essayer notre tchat !
            </a>

            <div id="monCadreAlert"></div>  
            <div id = "heure" class ="heure"></div>
            <div class="divFavorite" id="divFavorite" style="display:none">
            </div>
          
              



  <!-- Bootstrap core JavaScript -->
  <script src="/static/vendor/jquery/jquery.min.js"</script>
  <script src="/static/vendor/bootstrap/js/bootstrap.bundle.min.js"</script>

  <!-- Custom scripts for this template -->
  <script src="/static/styles/js/homegrandcat.js"></script>
{% endblock body %}
</body>

</html>



































