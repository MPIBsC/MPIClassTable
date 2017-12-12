<template>
  <div class="query">
    <el-form ref="form" status-icon inline>
      <el-form-item label="Program" prop="program">
        <el-select v-model="program" placeholder="Select your program" filterable>
          <el-option
            v-for="item in data.programs"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="Class Year" prop="classYear">
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
    <el-table :data="cls" style="width: 100%">
      <el-table-column prop="type" label="Type" width="58"></el-table-column>
      <el-table-column prop="class_code" label="Class Code" width="150"></el-table-column>
      <el-table-column prop="subject" label="Subject" width="180"></el-table-column>
      <el-table-column prop="instructor" label="Instructor" width="150"></el-table-column>
      <el-table-column prop="room" label="Room" width="210"></el-table-column>
      <el-table-column prop="time" label="Time" width="150"></el-table-column>
      <el-table-column prop="period" label="Period" width="180"></el-table-column>
      <el-table-column label="Time">
          <el-table-column label="Su" width="36">
            <template slot-scope="scope">
              <i class="el-icon-circle-check-outline" v-if="cond(scope.row.day.sun)"></i>
            </template>
          </el-table-column>
          <el-table-column label="Mo" width="36">
            <template slot-scope="scope">
              <i class="el-icon-circle-check-outline" v-if="cond(scope.row.day.mon)"></i>
            </template>
          </el-table-column>
          <el-table-column label="Tu" width="36">
            <template slot-scope="scope">
              <i class="el-icon-circle-check-outline" v-if="cond(scope.row.day.tue)"></i>
            </template>
          </el-table-column>
          <el-table-column label="We" width="36">
          <template slot-scope="scope">
            <i class="el-icon-circle-check-outline" v-if="cond(scope.row.day.wed)"></i>
          </template>
          </el-table-column>
          <el-table-column label="Th" width="36">
            <template slot-scope="scope">
              <i class="el-icon-circle-check-outline" v-if="cond(scope.row.day.thu)"></i>
            </template>
          </el-table-column>
          <el-table-column prop="day.fri" label="Fr" width="36">
            <template slot-scope="scope">
              <i class="el-icon-circle-check-outline" v-if="cond(scope.row.day.fri)"></i>
            </template>
          </el-table-column>
          <el-table-column prop="day.sat" label="Sa" width="36">
            <template slot-scope="scope">
              <i class="el-icon-circle-check-outline" v-if="cond(scope.row.day.sat)"></i>
            </template>
          </el-table-column>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data () {
    return {
      data: {
        programs: [],
        classYears: [1, 2, 3, 4]
      },
      program: null,
      yearSem: '2017_2018-2',
      classYear: null,
      cls: []
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
      this.$http.get('https://mpibsc.github.io/MPIClassTable/data/class/' +
        this.yearSem + '_' + this.classYear + '_' + this.program + '_ch.json'
        ).then(response => {
          this.cls = response.body
        }, response => {})
    },
    cond (val) {
      return val === 'true'
    }
  }
}
</script>

<style>

</style>
