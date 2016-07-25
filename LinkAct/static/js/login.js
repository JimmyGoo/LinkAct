$(document).ready(function() {
	var msg="";
	var elements = document.getElementsByTagName("INPUT");
	for (var i = 0; i < elements.length; i++) {
	    elements[i].oninvalid = function(e) {
	        if (!e.target.validity.valid) {
		        switch(e.target.id){
		            case 'password' : 
		            e.target.setCustomValidity("密码不能为空");
		            break;
		            case 'username' : 
		            e.target.setCustomValidity("用户名不能为空");
		            break;
		        default : e.target.setCustomValidity("");
		        break;

	        	}
	       	}
	    };

	    elements[i].oninput = function(e) {
        	e.target.setCustomValidity(msg);
    	};
	} 
})
