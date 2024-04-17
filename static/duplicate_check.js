// function checkDuplicate() {
//     var user_id = $('#id_user_id').val(); // Assuming user_id field id is 'id_user_id'
//     $.ajax({
//         type: 'POST',
//         url: '/check_duplicate_user_id/',
//         data: {
//             'user_id': user_id,
//             'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
//         },
//         success: function(response) {
//             if (response.exists) {
//                 $('#id_error').text('이미 사용 중인 아이디입니다.');
//             } else {
//                 $('#id_error').text('');
//             }
//         }
//     });
// }


$(document).ready(function() {
    $('#check-duplicate').click(function() {
        var usern_id = $('#id_user_id').val();
        $.ajax({
            url: '/check_userid/',
            data: {
                'user_id': user_id
            },
            dataType: 'json',
            success: function(data) {
                if (data.is_taken) {
                    $('#duplicate-result').text("이미 사용 중인 아이디입니다.");
                } else {
                    $('#duplicate-result').text("사용 가능한 아이디입니다.");
                }
            }
        });
    });
});