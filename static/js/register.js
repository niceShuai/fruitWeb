$(function(){

	var error_name = false;
	var error_password = false;
	var error_check_password = false;
	var error_email = false;
	var error_check = false;


	$('#user_name').blur(function() {
		check_user_name();
	});

	$('#pwd').blur(function() {
		check_pwd();
	});

	$('#cpwd').blur(function() {
		check_cpwd();
	});

	$('#email').blur(function() {
		check_email();
	});

	$('#allow').click(function() {
		if($(this).is(':checked'))
		{
			error_check = false;
			$(this).siblings('span').hide();
		}
		else
		{
			error_check = true;
			$(this).siblings('span').html('请勾选同意');
			$(this).siblings('span').show();
		}
	});


	function check_user_name(){
		var len = $('#user_name').val().length;
		var uname = $('#user_name').val();
		var $next_name = $('#user_name').next();
		if(len<5||len>20)
		{
			// $('#user_name').next().html(len)
			$next_name.html('请输入5-20个字符的用户名');
			$next_name.css({color:'red'}).show();
			error_name = true;
		}

		else {

            $.get("/user/register_search", {uname: uname}, function (data) {
                flag = data.flag;
                //flag为false时，说明此用户名未注册。flag为true时，说明此用户名已注册。
                if (flag) {
                    $next_name.html('此用户名已存在').css({color: 'red'}).show();
                    error_name = true;
                }
                else {
                    $next_name.html('此用户名可注册').css({color: 'green'}).show();
                    error_name = false;
                }
            });

        }

		//    下面为错误代码，这样写的话，在submit时，error_name再一次为false，
		// 在表单提交时，ajax请求的true还没回来，会造成用户名重复时也能提交表单。
		// else {
        //     $('#user_name').next().hide();
        //     error_name = false;
        //     alert('this is else');
        // }
		//
        // $.get("/user/register_search",{uname:uname},function (data) {
		// 	flag = data.flag;
		// 	//alert(flag); //flag为false时，说明此用户名未注册。flag为true时，说明此用户名已注册。
		// 	if (flag){
		// 		$next_name.html('此用户名已存在');
		// 		$next_name.css({color:'red'}).show();
		// 		error_name = true;
		// 		//此处error_name设置为true后，外面函数的error_name仍为false？
		// 		alert('ajax'+error_name);
		// 	}
		// 	else{
		// 		$next_name.html('此用户名可注册');
		// 		$next_name.css({color:'green'}).show();
		// 		error_name = false;
		// 		// alert('此用户名可注册');
		// 	}
        // });

		//alert('check'+error_name);
	}

	function check_pwd(){
		var len = $('#pwd').val().length;
		if(len<8||len>20)
		{
			$('#pwd').next().html('密码最少8位，最长20位');
			$('#pwd').next().show();
			error_password = true;
		}
		else
		{
			$('#pwd').next().hide();
			error_password = false;
		}		
	}


	function check_cpwd(){
		var pass = $('#pwd').val();
		var cpass = $('#cpwd').val();

		if(pass!=cpass)
		{
			$('#cpwd').next().html('两次输入的密码不一致');
			$('#cpwd').next().show();
			error_check_password = true;
		}
		else
		{
			$('#cpwd').next().hide();
			error_check_password = false;
		}		
		
	}

	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val()))
		{
			$('#email').next().hide();
			error_email = false;
		}
		else
		{
			$('#email').next().html('你输入的邮箱格式不正确');
			$('#email').next().show();
			error_check_password = true;
		}

	}


	// $('#reg_form').submit(function() {
	// 	check_user_name();
	// 	check_pwd();
	// 	check_cpwd();
	// 	check_email();
	//
	// 	if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false)
	// 	{
	// 		return true;
	// 	}
	// 	else
	// 	{
	// 		return false;
	// 	}
	//
	// });

		$('#btn').click(function() {
			check_user_name();
			check_pwd();
			check_cpwd();
			check_email();

			if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false)
			{
				return true;
			}
			else
			{
				return false;
			}

	});



});