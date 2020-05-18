$(document).ready(function () {
    $('.search_profil-js').on("input", function (e) {
        searchUser = $('.search_profil-js').val()
        $.ajax({
            method: "post",
            url: "/user",
            data: { search: searchUser },
            success: function (res) {
                if (searchUser == "") {
                    $('.profil_user-js').html("");
                } else if (res != "") {
                    $('.profil_user-js').html("");
                    $.each(res, function (index, value) {
                        data = '<div><img height="20px" width="20px" src="/static/uploads/' + value.id + "/avatar/" + value.avatar + '" alt=""><a href="/profil/' + value.id + '">' + value.username + '</a></div>'
                        $('.profil_user-js').append(data);
                    })
                }
            }
        })
    })
})