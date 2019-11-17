<template>
  <div class="home-container">
    <md-toolbar class="md-dense md-accent sticky" md-elevation="1">
      <h4>Ready to change the world?</h4>
      <div @click="logout" style="flex:2">
        <md-icon class="logout-icon">clear</md-icon>
      </div>
    </md-toolbar>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "home",
  data: () => ({}),
  props: ["baseUrl"],
  methods: {
    logout: function() {
      this.$router.push("login");
    }
  }
};
</script>

<style>
.home-container {
  display: inline-block;
  width: 100%;
}
.logout-icon {
  float: right;
  cursor: pointer;
}
.username-container {
  float: left;
  margin-left: 2%;
}
</style>