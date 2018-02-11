$(document).ready(function()
{
    var  grandpy =  (function($)
    {

            var __loader__ = $('#loader');
            var __answer__ = $('#answer ul');

            var run = function()
            {
                // initialized event
                init();
            };

            var init = function()
            {
                // user send question
               $(document).on('submit', '#form-1', search);
            };

            // search location
            var  search =  function(e)
            {
                e.stopPropagation();
                e.preventDefault();


                // get question
                var form_data = new FormData(this);
                var _url = $(this).attr('action');
                var form = $(this);
                var q = form_data.get('q');
                if( q != undefined && q != '') {
                    // active loader
                    __loader__.show();
                    // create id
                    var id = __answer__.children().length + 1;
                    // display question
                    var element = display_question(id, q);
                    // add id to form
                    form_data.append('id', id);
                    $.ajax({
                        url: _url,
                        type: 'POST',
                        data: form_data,
                        cache: false,
                        async: false,
                        contentType: false,
                        processData: false
                    }).done(function (data) {
                        $(element).append(data);
                       __answer__.animate({scrollTop: __answer__.height()}, 1000);
                        form[0].reset();
                    }).always(function () {
                        __loader__.hide();
                    });
                }
                return false;
            }

            // display question
            var display_question = function(id, q)
            {
                var element = document.createElement('li');
                element.setAttribute('id', 'q'+id);
                element.setAttribute('class', 'question');

                var html = '<div class="user bloc">' +
                    '                            <span class="id">Q'+id+'.</span><p>' +
                    '                                <span class="name">Vous : </span><br/>' +
                                                    q +
                    '                            </p>' +
                    '                        </div>';
                element.innerHTML = html;
               $( __answer__).append(element);
                return element;
            };

            return {
                run: run,
            };

        })(jQuery);


   grandpy.run();
})