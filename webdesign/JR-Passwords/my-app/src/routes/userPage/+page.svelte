<script>
    import Navbar from "../navbar.svelte";
    import PasswordCard from "../passwordCard.svelte";
    import AddPassword from "../addPassword.svelte";
</script>

<body>
    <div id="main">
        <Navbar/>
        <h1 id="yourPasw">Your passwords:</h1>
        <div id="paswContainer">
            <div class="paswList" id="paswCard">
                <PasswordCard/>
            </div> 
            <div class="paswList" id="addPasw">
                <AddPassword/>
            </div>
        </div>
    </div>
</body>

<style>
    #main{
        display: flex;
        flex-direction: column;
        padding: 75px;
    }
    #paswContainer{
        justify-content: space-between;
    }
</style>