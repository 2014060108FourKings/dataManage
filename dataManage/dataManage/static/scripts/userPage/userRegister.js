/**
 * Created by qq12cvhj on 16-11-1.
 */

 function userRegister(){
        var registerData = {
//Note：！！！这地方有点问题，json的值只能先通过stringify才能打到后台被flask的json解析，而在node.js和java中普通的json传就OK。暂时通过stringify解决，后面再看其他东西。
        data:JSON.stringify({
            "userName" : $("#userName").val(),
            "password" :  $("#password").val(),
            "name" : $("#name").val()
        })
    };
        $.ajax(
                {
                    url:"/reg",
                    type: 'POST',
                    data: registerData,
                    success: function (msg) {
                        if(msg=='success'){
                            window.location = '/userLogin'
                        }
                        else {
                            document.getElementById("registerTips").innerText = msg
                        }
                    }
                }
        )
    }