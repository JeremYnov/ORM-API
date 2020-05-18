$(document).ready(function(){
    $('.search_bar-js').on("input",function(e){
        user = $('.search_bar-js').val()
        $.ajax({
            method:"post",
            url:"/user",
            data:{text:user},
            success:function(res){
                if(res != ""){
                    $('.result_user_js').html("");
                    $.each(res,function(index,value) {          
                        data = '<div class="search-user"><img height="20px" width="20px" src="../../../static/img/' + value.avatar + '" alt=""><a href="/talk/' + value.id + '">' + value.username + '</a></div>'
                        $('.result_user_js').append(data);
                    })
                }else{
                    console.log(1)
                    $('.result_user_js').html("<div class='alert alert-warning' role='alert'>Aucun utilisateurs</div>") ;
                }
            }
        })
    })
})