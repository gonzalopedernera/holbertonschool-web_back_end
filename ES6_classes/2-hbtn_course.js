export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name === 'string') {
      this._name = name;
    }
    if (typeof length === 'number') {
      this._length = length;
    }
    if (Array.isArray(students)) {
      this._students = students;
    }
  }

  set name(name) {
    this._name = name;
  }
  get name() {
    return this._name;
  }

  set length(length) {
    this._length = length;
  }
  get length() {
    return this._length;
  }

  set students(students) {
    this._students = students;
  }
  get students() {
    return this._students;
  }
}