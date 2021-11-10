Vue.component('list-transact', {
    template: '<div class="col-12 transact-item">New Item</div>'
})

var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue!',
        mostrar: true
    },
    delimiters: ['[[', ']]']
});