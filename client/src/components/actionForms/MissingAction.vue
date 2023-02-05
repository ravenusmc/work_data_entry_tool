<template>
  <div>
    <form class="contact-form" @submit="submitAction">
      <div class="form-group">
        <label for="firstname">Recruit Action:</label>
        <select v-model="selectedValueRecruitAction">
          <option disabled value="">Please select one</option>
          <option v-for="item in recruit_action" :key="item" :value="item">
            {{ item }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label for="NOA">Nature of Action:</label>
        <input
          type="text"
          name="NOA"
          class="form-control"
          id="NOA"
          v-model="NOA"
        />
      </div>
      <div class="form-group">
        <label for="Authority">Authority:</label>
        <input
          type="text"
          name="Authority"
          class="form-control"
          id="Authority"
          v-model="Authority"
        />
      </div>
      <div class="form-group">
        <label for="Date_Receieved">Date Receieved:</label>
        <input
          type="date"
          name="ienumber"
          class="form-control"
          id="Date_Receieved"
          v-model="Date_Receieved"
        />
      </div>
      <div class="form-group">
        <label for="firstname">Action Returned:</label>
        <select v-model="selectedValueReturned">
          <option disabled value="">Please select one</option>
          <option v-for="item in Returned" :key="item" :value="item">
            {{ item }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label for="Keyed">Action Keyed:</label>
        <select v-model="selectedValueKeyed">
          <option disabled value="">Please select one</option>
          <option v-for="item in Keyed" :key="item" :value="item">
            {{ item }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label for="firstname">Action Applied:</label>
        <select v-model="selectedValueApplied">
          <option disabled value="">Please select one</option>
          <option v-for="item in Applied" :key="item" :value="item">
            {{ item }}
          </option>
        </select>
      </div>

      <div class="btn-div">
        <button @click.prevent="submitAction" type="submit" name="login" class="btn btn-primary button-fix">
          Submit
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "ActionsForm",
  computed: {
    ...mapGetters("data", ["actionNumber", "actionID"]),
    ...mapGetters("session", ["userObject"]),
  },
  data() {
    return {
      recruit_action: [true, false],
      selectedValueRecruitAction: null,
      action_number: "",
      NOA: "",
      Authority: "",
      Processor_ieNumber: "", // Get from user
      Date_Receieved: "",
      Returned: [true, false],
      selectedValueReturned: null,
      Keyed: [true, false],
      selectedValueKeyed: null,
      Applied: [true, false],
      selectedValueApplied: null,
    };
  },
  methods: {
    ...mapActions("data", ["submitActionToDatabase"]),
     submitAction() {
      const payload = {
        action_id: this.actionID,
        user_id: this.userObject['id'],
        recruit_action: this.selectedValueRecruitAction,
        action_number: this.actionNumber,
        NOA: this.NOA,
        Authority: this.Authority,
        Processor_ieNumber: this.userObject['ieNumber'],
        Date_Receieved: this.Date_Receieved,
        Returned: this.selectedValueReturned,
        Keyed: this.selectedValueKeyed,
        Applied: this.selectedValueApplied
      };
      this.submitActionToDatabase({ payload });
    },
  },
};
</script>

<style scoped>
.contact-form {
  display: grid;
  gap: 1.25rem;
  grid-template-columns: 1fr 1fr;
  margin: 3% 20% 3% 20%;
}

.form-group {
  display: grid;
}

.button-fix {
  width: 100px;
  height: 50px;
}
</style>