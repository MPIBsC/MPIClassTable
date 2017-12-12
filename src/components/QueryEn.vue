<template>
  <div class="query">
    <el-form ref="form">
      <!-- <el-form-item>
        <el-select v-model="school" placeholder="School">
          <el-option
            v-for="item in data.schools"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
      </el-form-item> -->
      <el-form-item>
        <el-select v-model="program" placeholder="Program">
          <el-option
            v-for="item in data.programs"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-select v-model="classYear" placeholder="Year/Semester">
          <el-option
            v-for="item in data.classYears"
            :key="item"
            :value="item">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="query">Query</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  data () {
    return {
      data: {
        schools: [],
        programs: [],
        yearSems: [{value: 1, label: '2017/2018-2'}],
        classYears: [1, 2, 3, 4]
      },
      school: null,
      program: null,
      yearSem: null,
      classYear: null
    }
  },
  mounted () {
    this.getSchools()
    this.getPrograms()
  },
  methods: {
    getSchools () {
      this.$http.get('https://mpibsc.github.io/MPIClassTable/data/school.json').then(response => {
        this.data.schools = response.body
      }, response => {})
    },
    getPrograms () {
      this.$http.get('https://mpibsc.github.io/MPIClassTable/data/programs.json').then(response => {
        this.data.programs = response.body
      }, response => {})
    },
    query () {

    }
  }
}
</script>

<style>

</style>
