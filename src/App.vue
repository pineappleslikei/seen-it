<template>
  <div>
    <div id="nav">
      <div id="nav-left">
        <img id="logo" src="./assets/mylogo.png" alt="" />
      </div>
      <div id="nav-right">
        <router-link :to="{ name: 'Home' }">Home</router-link> |
        <router-link :to="{ name: 'Search' }">Search</router-link> |
        <router-link :to="{ name: 'Profile' }">Profile</router-link>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
  padding: 5px;
}

#nav a.router-link-exact-active {
  color: whitesmoke;
}
#nav {
  background-color: #1098f7;
  color: white;
  display: flex;
  justify-content: space-between;
}
#logo {
  width: 125px;
}
#nav-right {
  display: flex;
  justify-content: center;
  align-items: center;
  padding-right: 20px;
}
.nav-item {
  padding: 8px;
  margin: 0px;
}
</style>
