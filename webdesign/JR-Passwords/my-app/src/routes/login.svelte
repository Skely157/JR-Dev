<style>
    #login-container{
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 50px;
    }
</style>


<body>
    <div id="login-container">
        <h2>Login</h2>
        <form action="changeStatus()" method="POST">
            <div class="login-group">
                <label for="username">Username:</label><br>
                <input type="text" id="username" name="username" required><br>
            </div>
            <div class="login-group">
                <label for="password">Password:</label><br>
                <input type="password" id="password" name="password" required><br><br>
            </div>
            <button type="submit">{buttonStatus}</button>
        </form>
    </div>
</body>

<script>
    let buttonStatus = "Submit";

    function changeStatus(){
        let buttonStatus = "Success"
        return
    }
</script>
