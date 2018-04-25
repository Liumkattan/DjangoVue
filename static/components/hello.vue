<template>
    <div class="hello">Hello from {{who}}</div>
</template>
 
<script>
module.exports = {
    data: function() {
        return {
            who: 'Vue Component!!'
        }
    }
}
</script>
 
<style>
.hello {
    background-color: #eee;
}
</style>