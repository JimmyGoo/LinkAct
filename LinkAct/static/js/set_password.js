$(document).ready(function() {
	var msg="";
	var elements = document.getElementsByTagName("INPUT");
	for (var i = 0; i < elements.length; i++) {
	    elements[i].oninvalid = function(e) {
	        if (!e.target.validity.valid) {
		        switch(e.target.id){
		            case 'new_password1' : 
		            e.target.setCustomValidity("新密码不能为空");
		            break;
		            case 'new_password2' : 
		            e.target.setCustomValidity("请再次输入新密码");
		            break;
		  			case 'origin_password':
		            e.target.setCustomValidity("请输入原始密码");
		            break;
		        default : e.target.setCustomValidity("此处不能为空");
		        break;

	        	}
	       	}
	    };

	    elements[i].oninput = function(e) {
        	e.target.setCustomValidity(msg);
        	if(e.target.id == email)
        	{

        	}
    	};
	} 
});