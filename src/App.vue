<template>
  <div id="app">
    <el-container>
    <el-header>
      <el-menu :default-active="'1'" class="el-menu-demo" mode="horizontal">
        <el-menu-item index="1">MPI Class Table</el-menu-item>
      </el-menu>
    </el-header>
    <el-main>
      <router-view/>
    </el-main>
    <el-footer>
        <!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/MPIBsC/MPIClassTable/subscription" data-icon="octicon-eye" data-size="large" aria-label="Watch MPIBsC/MPIClassTable on GitHub">Watch</a>
<!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/MPIBsC/MPIClassTable/issues" data-icon="octicon-issue-opened" data-size="large" aria-label="Issue MPIBsC/MPIClassTable on GitHub">Issue</a>
      <p>(c) 2017 MPIBsC, data provided by <a href="https://wapps.ipm.edu.mo/siweb/time_prog.asp">MPI - Class Timetable Enquiry</a></p>
    </el-footer>
  </el-container>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.raw {
  display: none;
}
</style>
