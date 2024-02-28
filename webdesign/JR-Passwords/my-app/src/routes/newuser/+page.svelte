<style>
    #create-container{
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 50px;
    }
</style>


<body>
    <div id="create-container">
        <h2>Create new user</h2>
        <form action="/newuser/success">
            <div class="info-group">
                <label for="username">Username:</label><br>
                <input type="text" id="username" name="username" required><br>
            </div>
            <div class="info-group">
                <label for="password">Password:</label><br>
                <input type="password" id="password" name="password" required><br><br>
            </div>
            <button type="submit">Submit</button>
        </form>
    </div>
</body>