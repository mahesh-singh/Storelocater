var locationModule = (function (JQ) {

  return {
 
    init: function(){
		JQ('#hrefAddLocations').on('click', function(){
			alert("click");
		})		
	}
  };
 
})(jQuery);

$(document).ready(function(){
	locationModule.init();
});
