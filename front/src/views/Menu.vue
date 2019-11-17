<template>
  <div class="features-container">
    <md-card md-with-hover class="feature">
      <router-link to="fast">
        <md-card-header>
          <div class="md-title">Fast Tracking</div>
        </md-card-header>
        <md-card-content class="card-content">
          <span>Upload one or more images of different places and generate a heatmap of plastic waste</span>
        </md-card-content>
      </router-link>
    </md-card>
    <md-card md-with-hover class="feature">
      <router-link to="impact">
        <md-card-header>
          <div class="md-title">Impact measurement</div>
        </md-card-header>
        <md-card-content class="card-content">
          <span>Upload images of the same place before and after garbage collecting actions</span>
        </md-card-content>
      </router-link>
    </md-card>
    <md-card md-with-hover class="feature">
      <router-link to="catalogue">
        <md-card-header>
          <div class="md-title">My catalogue</div>
        </md-card-header>
        <md-card-content class="card-content">
          <span>Review all your uploaded resources</span>
        </md-card-content>
      </router-link>
    </md-card>
  </div>
</template>

<script>
export default {
  name: "menu",
  data: () => ({}),
  props: ["baseUrl"]
};
</script>

<style>
.features-container {
  margin: 0 auto;
  width: 60%;
}
.feature {
  margin: 0 auto;
  margin-top: 5vh;
  width: 30%;
}
.card-content {
  text-align: justify;
}
h4 {
  margin: 0;
}
@media only screen and (max-width: 1400px) {
  .feature {
    width: 50%;
  }
}
@media only screen and (max-width: 700px) {
  .feature {
    width: 100%;
  }
}
</style>