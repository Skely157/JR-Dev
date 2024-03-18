<style>
    #main{
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    #addPaswContainer{
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-style: solid;
        border-width: 3px;
        border-color: black;
        border-radius: 10px;
        margin: 20px;
    }
    h2{
        padding: 10px;
    }
    p{
        padding: 5px;
    }
    button{
	background: none;
	color: inherit;
	border: none;
	padding: 0;
	font: inherit;
	cursor: pointer;
	outline: inherit;
    }
</style>


<div id="main">
    {#each passwordCards as _, i}
        <AddPasswordForm key={i}/>
    {/each}
    <div id="addPaswContainer">
        <button on:click={addPasswordCard}><h2>+</h2></button>
        <p>Add a new password</p>
    </div>
</div>

<script lang="ts">
    import AddPasswordForm from "./addPasswordForm.svelte";

    let passwordCards = [];

    function addPasswordCard() {
        passwordCards= [...passwordCards, {}];
    }
</script>