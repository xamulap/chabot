<html>
<head>
  <link rel="stylesheet" type="text/css" href="style.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
</head>
<body>
	<div class="wrap">
	<div class="cat">
	  <div class="eyes">
	    <div class="eye"></div>
	    <div class="eye two"></div>
	  </div>
	  <div class="mouth" id="mouth">
	    <div class="lezu"></div>
	  </div>
	</div>
	<div class="shadow"></div>
	</div>
</body>
<script>
function random(min, max) {
  return Math.floor(Math.random() * (max - min + 1) ) + min;
}

  $(window).on('load', function(){
        console.log("go");
	$(".cat").click(function() { 
		for(var i=0;i<random(1,10);i++) { 
			var delay = random(100,200)
		      $(".mouth").animate({height:"80px"},delay).animate({height:"50px"},delay);
		}
	});
  });
</script>


</html>
