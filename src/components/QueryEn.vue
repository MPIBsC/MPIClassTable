<template>
  <div class="query">
    <el-form ref="form">
      <el-form-item>
        <el-select v-model="school" placeholder="School">
          <el-option
            v-for="item in data.schools"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
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
        <el-select v-model="yearSem" placeholder="Year/Semester">
          <el-option
            v-for="item in data.yearSems"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
        <el-select v-model="classYear" placeholder="Year/Semester">
          <el-option
            v-for="item in data.classYears"
            :key="item.value"
            :label="item.label"
            :value="item.value">
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
import schools from '../../data/school.json'
import programs from '../../data/programs.json'
export default {
  data () {
    return {
      data: {
        schools: schools,
        programs: programs,
        yearSems: [{value: 1, label: '2017/2018-2'}],
        classYears: [{value: 1, label: '1'}]
      },
      school: null,
      program: null,
      yearSem: null,
      classYears: null
    }
  },
  methods: {
    getSchool () {
    }
  }
}
</script>

<style>

</style>
