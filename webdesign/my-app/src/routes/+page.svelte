<h1>Welcome to JR-Bots</h1>

<p id="test">Julian Tester 123</p>

<script>
    let counter = 0
    function increaseCounter(){
        counter += 1
    }
</script>

<button on:click={increaseCounter}>Du har klikket {counter} ganger :) </button>

<style>
    #test {
        color: red;
    }

    :global(body) {
        background-color: gray;
    
    }

</style>
