$("document").ready (
    function () {
        $(".comment-like").on(types:"click", selector:function() {
            let comment_id = $(this).attr(name:"id");

            $.ajax(url:{
                "url":"/shop/add-ajax-like/",
                "data":{"hello":true},
                "method":"get",
                success:function (data) {
                    console.log(data)
                },
                error: function (data) {
                    console.log("hello error", data)
                }
            });
            console.log(comment_id)
        })

    }
);
