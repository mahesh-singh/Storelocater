var locationModule = (function (JQ) {

  return {
 
    init: function(){

    	JQ('#hrefAddLocations').on('click', function(){
    		$('#locationModal').modal('show');
    	});

		  JQ('#locationModal').on('show.bs.modal', function (event) {
			 JQ('#div-modal-content').load('/location/add', function(){
        $(function () {
          $('[data-toggle="tooltip"]').tooltip()
        })
      });
		});		
	}
  };
 
})(jQuery);

$(document).ready(function(){
	locationModule.init();
});
