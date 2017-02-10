 var i=0; 
 function clusterOutliers() {
      network.setData(data);
	   var clusterOptionsByData = {
          processProperties: function(clusterOptions, childNodes) {
            clusterOptions.label = "cetaitlenom";
            return clusterOptions;
          },
          clusterNodeProperties: {borderWidth:3, shape:'box', font:{size:30}}
      };

      network.clusterOutliers(clusterOptionsByData);
      network.clusterOutliers(clusterOptionsByData);
      network.clusterOutliers(clusterOptionsByData);
 }

function clusterByHubsize() {
      network.setData(data);
      var clusterOptionsByData = {
          processProperties: function(clusterOptions, childNodes) {
            clusterOptions.label = "[" + childNodes.length + "]";
            return clusterOptions;
          },
          clusterNodeProperties: {borderWidth:3, shape:'box', font:{size:30}}
      };
      network.clusterByHubsize(undefined, clusterOptionsByData);
  }
function visnetwork(num) {
 // create a network

  var container = document.getElementById('BlockOnto_'+num);
  var data = {
    nodes: nodes,
    edges: edges
  };
   

  var options = {layout:{randomSeed:4}, physics :false};
  var network = new vis.Network(container, data, options);
  network.on("selectNode", function(params) {
      if (params.nodes.length == 1) {
          if (network.isCluster(params.nodes[0]) == true) {
              network.openCluster(params.nodes[0]);
          }
      }
  });

 }
 function display(){
  if ( display === true ) {
  $( '.Button_Onto_'+count).show();
} else if ( display === false ) {
  $( '.Button_Onto_'+count ).hide();
}
	 
 }
 function hideVSdiplay(count) {
	
	if ($('#BlockGlobalOnto'+count).hasClass("goAway")) {
	$('#BlockGlobalOnto'+count).removeClass("goAway");
	
	}
	else {
	$( '#BlockGlobalOnto'+count).addClass("goAway");
	}
	
   $('.Button_Onto_'+count).toggle( display );;
  }
  
$('.fixed-action-btn').openFAB();
$('.fixed-action-btn').closeFAB();
$('.fixed-action-btn.toolbar').openToolbar();
$('.fixed-action-btn.toolbar').closeToolbar();
 

function addURL(){
	$('#addurl' ).append( '<div id="linkURL" class="linkU input-field col s6"><i class="material-icons prefix">link</i><input id="icon_prefix" type="text" name="textLink" class="link"><label for="icon_prefix">URL ontologie</label></div>' );
		
 $('.linkU:last').each(function(){
    i++;
    var newID='linkURL'+i+' ';
    $(this).attr('id',newID);
    });
	
}