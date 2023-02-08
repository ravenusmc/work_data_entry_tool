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
        <label for="title">Title:</label>
        <input
          type="text"
          name="title"
          class="form-control"
          id="title"
          v-model="title"
        />
      </div>
      <div class="form-group">
        <label for="create_date">Create Date:</label>
        <input
          type="date"
          name="create_date"
          class="form-control"
          id="create_date"
          v-model="create_date"
        />
      </div>
      <div class="form-group">
        <label for="create_date">Effective Date:</label>
        <input
          type="date"
          name="effective_date"
          class="form-control"
          id="effective_date"
          v-model="effective_date"
        />
      </div>
      <div class="form-group">
        <label for="create_date">Received by Class Date:</label>
        <input
          type="date"
          name="received_by_class"
          class="form-control"
          id="received_by_class"
          v-model="received_by_class"
        />
      </div>
      <div class="form-group">
        <label for="received_by_staffing">Received by Staffing Date:</label>
        <input
          type="date"
          name="received_by_staffing"
          class="form-control"
          id="received_by_staffing"
          v-model="received_by_staffing"
        />
      </div>
      <div class="form-group">
        <label for="received_by_processing">Received by Processing Date:</label>
        <input
          type="date"
          name="received_by_processing"
          class="form-control"
          id="received_by_processing"
          v-model="received_by_processing"
        />
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
        <button
          @click.prevent="submitAction"
          type="submit"
          name="login"
          class="btn btn-primary button-fix"
        >
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
      title: "",
      create_date: "",
      effective_date: "",
      received_by_class: "",
      received_by_staffing: "",
      received_by_processing: "",
      NOA: "",
      Authority: "",
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
    ...mapActions("data", ["submitActionToDatabase", "submitMissingActionToDatabase"]),
    submitAction() {
      const payload = {
        action_number: this.actionNumber,
        user_id: this.userObject["id"],
        selectedValueRecruitAction: this.selectedValueRecruitAction,
        title: this.title,
        create_date: this.create_date,
        effective_date: this.effective_date,
        received_by_class: this.received_by_class,
        received_by_staffing: this.received_by_staffing,
        received_by_processing: this.received_by_processing,
        NOA: this.NOA,
        Authority: this.Authority,
        Processor_ieNumber: this.userObject['ieNumber'],
        Date_Receievd: this.Date_Receieved,
        Returned: this.selectedValueReturned,
        Keyed: this.selectedValueKeyed,
        Applied: this.selectedValueApplied,
      };
      console.log(payload);
      // this.submitMissingActionToDatabase({ payload });
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