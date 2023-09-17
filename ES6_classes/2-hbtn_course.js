export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name === 'string') {
      this._name = name;
    }
    else {
      throw new TypeError("Name must be a string");
    }
    if (typeof length === 'number') {
      this._length = length;
    }
    else {
      throw new TypeError("Length must be a number");
    }
    if (Array.isArray(students)) {
      this._students = students;
    }
    else {
      throw new TypeError("Students must be an array");
    }
  }

  set name(name) {
    if (typeof name === 'string') {
      this._name = name;
    }
    else {
      throw new TypeError("Name must be a string");
    }
  }
  get name() {
    return this._name;
  }

  set length(length) {
    if (typeof length === 'number') {
      this._length = length;
    }
    else {
      throw new TypeError("Length must be a number");
    }
  }
  get length() {
    return this._length;
  }

  set students(students) {
    if (Array.isArray(students)) {
      this._students = students;
    }
    else {
      throw new TypeError("Students must be an array");
    }
  }
  get students() {
    return this._students;
  }
}