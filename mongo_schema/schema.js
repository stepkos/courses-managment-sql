db.createCollection("faculties", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["_id", "name", "email"],
      properties: {
        _id: {
          bsonType: "objectId",
          description: "Faculty ID must be an objectId"
        },
        name: {
          bsonType: "string",
          description: "Faculty name must be a string"
        },
        email: {
          bsonType: "string",
          pattern: "^.+@.+$",
          description: "Email must be a valid email address"
        },
        phone: {
          bsonType: "string",
          pattern: "^(\\+\\d{1,3}[- ]?)?\\(?\\d{1,4}\\)?[- ]?\\d{1,4}[- ]?\\d{1,4}([- ]?\\d{1,4})?$",
          description: "Phone number must be a valid phone number format"
        },
        website: {
          bsonType: "string",
          pattern: "^(https?|ftp)://.+",
          description: "Website must be a valid URL"
        },
        faculty_administrators: {
          bsonType: "array",
          items: {
            bsonType: "object",
            required: ["_id"],
            properties: {
              _id: {
                bsonType: "objectId",
                description: "Administrator ID must reference a document in the users collection"
              }
            }
          }
        },
        fields_of_study: {
          bsonType: "array",
          items: {
            bsonType: "object",
            required: ["name", "start_year", "created_by", "created_at"],
            properties: {
              name: {
                bsonType: "string",
                description: "Field of study name must be a string"
              },
              description: {
                bsonType: "string",
                description: "Description must be a string"
              },
              start_year: {
                bsonType: "int",
                minimum: 1900,
                description: "Start year must be an integer >= 1900"
              },
              created_by: {
                bsonType: "objectId",
                description: "Created by must reference a document in the users collection"
              },
              created_at: {
                bsonType: "date",
                description: "Created at must be a date"
              },
              terms: {
                bsonType: "array",
                items: {
                  bsonType: "object",
                  required: ["term_number", "created_by", "created_at"],
                  properties: {
                    term_number: {
                      bsonType: "int",
                      minimum: 1,
                      description: "Term number must be an integer >= 1"
                    },
                    created_by: {
                      bsonType: "objectId",
                      description: "Created by must reference a document in the users collection"
                    },
                    created_at: {
                      bsonType: "date",
                      description: "Created at must be a date"
                    },
                    courses: {
                      bsonType: "array",
                      items: {
                        bsonType: "object",
                        required: ["_id", "title", "created_by", "created_at"],
                        properties: {
                          _id: {
                            bsonType: "objectId",
                            description: "Course ID must be na objectId"
                          },
                          title: {
                            bsonType: "string",
                            description: "Title must be a string"
                          },
                          description: {
                            bsonType: "string",
                            description: "Description must be a string"
                          },
                          created_by: {
                            bsonType: "objectId",
                            description: "Created by must reference a document in the users collection"
                          },
                          created_at: {
                            bsonType: "date",
                            description: "Created at must be a date"
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
});



db.createCollection("users", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["_id", "first_name", "last_name", "email", "password"],
      properties: {
        _id: {
          bsonType: "objectId",
          description: "User ID must be an objectId"
        },
        first_name: {
          bsonType: "string",
          description: "First name must be a string"
        },
        last_name: {
          bsonType: "string",
          description: "Last name must be a string"
        },
        email: {
          bsonType: "string",
          pattern: "^.+@.+$",
          description: "Email must be a valid email address"
        },
        password: {
          bsonType: "string",
          description: "Password must be a string"
        },
        is_active: {
          bsonType: "bool",
          description: "Is active must be a boolean"
        },
        degree: {
          bsonType: "string",
          enum: ["Bachelor", "Master", "PhD"],
          description: "Degree must be one of the following: 'Bachelor', 'Master', or 'PhD'"
        },
        profile_type: {
          bsonType: "int",
          description: "Profile type must be an integer"
        },
        courses_hosted: {
          bsonType: "array",
          items: {
            bsonType: "object",
            required: ["course_id", "is_admin", "created_by", "created_at"],
            properties: {
              course_id: {
                bsonType: "objectId",
                description: "Course ID must be a reference to a course document in the 'faculties' collection"
              },
              is_admin: {
                bsonType: "bool",
                description: "Is admin must be a boolean"
              },
              created_by: {
                bsonType: "objectId",
                description: "Created by must be a reference to a user document"
              },
              created_at: {
                bsonType: "date",
                description: "Created at must be a date"
              }
            }
          }
        },
        groups_hosted: {
          bsonType: "array",
          items: {
            bsonType: "objectId",
            description: "Group ID must be a reference to a document in the 'groups' collection"
          }
        }
      }
    }
  }
});


db.createCollection("groups", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["_id", "name", "created_by", "college_term", "assigned_to_course_id"],
      properties: {
        _id: {
          bsonType: "objectId",
          description: "Group ID must be an objectId"
        },
        name: {
          bsonType: "string",
          description: "Name must be a string"
        },
        description: {
          bsonType: "string",
          description: "Description must be a string"
        },
        image: {
          bsonType: "string",
          pattern: "^(https?:\\/\\/)?[\\da-z.-]+\\.[a-z.]{2,6}([\\/\\w .-]*)*\\/?$",
          description: "Image must be a valid URL or null"
        },
        created_by: {
          bsonType: "objectId",
          description: "Created_by must reference a user document"
        },
        created_at: {
          bsonType: "date",
          description: "Created_at must be a date"
        },
        college_term: {
          bsonType: "object",
          required: ["start_date", "end_date"],
          properties: {
            start_date: {
              bsonType: "date",
              description: "Start_date must be a date"
            },
            end_date: {
              bsonType: "date",
              description: "End_date must be a date"
            }
          }
        },
        assigned_to_course_id: {
          bsonType: "objectId",
          description: "Assigned_to_course_id must reference a course document in the faculties collection"
        },
        students: {
          bsonType: "array",
          items: {
            bsonType: "object",
            required: ["student_id", "first_name", "last_name", "assigned_by", "assigned_at"],
            properties: {
              student_id: {
                bsonType: "objectId",
                description: "Student_id must reference a user document"
              },
              first_name: {
                bsonType: "string",
                description: "First_name must be a string"
              },
              last_name: {
                bsonType: "string",
                description: "Last_name must be a string"
              },
              assigned_by: {
                bsonType: "objectId",
                description: "Assigned_by must reference a user document"
              },
              assigned_at: {
                bsonType: "date",
                description: "Assigned_at must be a date"
              }
            }
          }
        }
      }
    }
  }
});


db.createCollection("attempts", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["_id", "student_id", "test_id", "started_at"],
      properties: {
        _id: {
          bsonType: "objectId",
          description: "Attempt ID must be an objectId"
        },
        student_id: {
          bsonType: "objectId",
          description: "Student ID must reference a document in the users collection"
        },
        test_id: {
          bsonType: "objectId",
          description: "Test ID must reference a document in the tests collection"
        },
        score: {
          bsonType: ["double", "null"],
          minimum: 0,
          maximum: 100,
          description: "Score must be a number between 0 and 100 or null"
        },
        grade: {
          bsonType: "double",
          enum: [2.0, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5],
          description: "Grade must be one of the specified values: 2.0, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5"
        },
        started_at: {
          bsonType: "date",
          description: "Started_at must be a date"
        },
        submitted_at: {
          bsonType: "date",
          description: "Submitted_at must be a date"
        },
        answers_for_open_q: {
          bsonType: "array",
          items: {
            bsonType: "object",
            required: ["open_q_id", "content", "points"],
            properties: {
              open_q_id: {
                bsonType: "objectId",
                description: "Open_q_id must reference a document in the open_questions collection"
              },
              content: {
                bsonType: "string",
                description: "Content must be a string"
              },
              points: {
                bsonType: "int",
                description: "Points must be an integer"
              }
            }
          }
        },
        answers_for_closed_q: {
          bsonType: "array",
          items: {
            bsonType: "object",
            required: ["closed_q_id", "choice"],
            properties: {
              closed_q_id: {
                bsonType: "objectId",
                description: "Closed_q_id must reference a document in the closed_questions collection"
              },
              choice: {
                bsonType: "string",
                description: "Choice must be a string"
              }
            }
          }
        }
      }
    }
  }
});



db.createCollection("entries", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["_id", "group_id", "title", "created_at"],
      properties: {
        _id: {
          bsonType: "objectId",
          description: "Entry ID must be an ObjectId"
        },
        group_id: {
          bsonType: "objectId",
          description: "Group ID must be an ObjectId"
        },
        title: {
          bsonType: "string",
          description: "Title must be a string"
        },
        created_at: {
          bsonType: "date",
          description: "Created at must be a date"
        },
        created_by: {
          bsonType: "objectId",
          description: "Created by must be a reference to a User ID"
        },
        updated_at: {
          bsonType: "date",
          description: "Updated at must be a date"
        },
        content: {
          bsonType: "string",
          description: "Content must be a string"
        },
        file_url: {
          bsonType: "string",
          pattern: "^(https?:\\/\\/)?[\\da-z.-]+\\.[a-z.]{2,6}([\\/\\w .-]*)*\\/?$",
          description: "File URL must be a valid URL"
        },
        exercise: {
          bsonType: "object",
          required: ["exercise_id", "due_date"],
          properties: {
            exercise_id: {
              bsonType: "objectId",
              description: "Exercise ID"
            },
            due_date: {
              bsonType: "date",
              description: "Due date must be a date"
            }
          }
        },
        test: {
          bsonType: "object",
          required: ["test_id", "title", "available_from_date", "available_to_date"],
          properties: {
            test_id: {
              bsonType: "objectId",
              description: "Test ID"
            },
            title: {
              bsonType: "string",
              description: "Title must be a string"
            },
            description: {
              bsonType: "string",
              description: "Description must be a string"
            },
            available_from_date: {
              bsonType: "date",
              description: "Available from date must be a date"
            },
            available_to_date: {
              bsonType: "date",
              description: "Available to date must be a date"
            },
            max_seconds_for_open: {
              bsonType: "int",
              description: "Max seconds for open questions must be an integer"
            },
            max_seconds_for_closed: {
              bsonType: "int",
              description: "Max seconds for closed questions must be an integer"
            },
            duration_in_minutes: {
              bsonType: "int",
              description: "Duration in minutes must be an integer"
            },
            closed_questions: {
              bsonType: "array",
              items: {
                bsonType: "object",
                required: ["closed_q_id", "content", "choices"],
                properties: {
                  closed_q_id: {
                    bsonType: "objectId",
                    description: "Closed question ID"
                  },
                  content: {
                    bsonType: "string",
                    description: "Content must be a string"
                  },
                  points: {
                    bsonType: "int",
                    description: "Points must be an integer"
                  },
                  choices: {
                    bsonType: "array",
                    items: {
                      bsonType: "object",
                      required: ["designation", "content", "is_correct"],
                      properties: {
                        designation: {
                          bsonType: "string",
                          description: "Choice designation must be a string"
                        },
                        content: {
                          bsonType: "string",
                          description: "Choice content must be a string"
                        },
                        is_correct: {
                          bsonType: "bool",
                          description: "Is correct must be a boolean"
                        }
                      }
                    }
                  }
                }
              }
            },
            open_questions: {
              bsonType: "array",
              items: {
                bsonType: "object",
                required: ["open_q_id", "content"],
                properties: {
                  open_q_id: {
                    bsonType: "objectId",
                    description: "Open question ID"
                  },
                  content: {
                    bsonType: "string",
                    description: "Content must be a string"
                  },
                  points: {
                    bsonType: "int",
                    description: "Points must be an integer"
                  }
                }
              }
            }
          }
        },
        comments: {
          bsonType: "array",
          items: {
            bsonType: "object",
            required: ["user", "content", "created_at"],
            properties: {
              user: {
                bsonType: "object",
                required: ["user_id", "first_name", "last_name"],
                properties: {
                  user_id: {
                    bsonType: "objectId",
                    description: "User ID must be a reference to a User ID"
                  },
                  first_name: {
                    bsonType: "string",
                    description: "First name must be a string"
                  },
                  last_name: {
                    bsonType: "string",
                    description: "Last name must be a string"
                  }
                }
              },
              content: {
                bsonType: "string",
                description: "Content must be a string"
              },
              created_at: {
                bsonType: "date",
                description: "Created at must be a date"
              }
            }
          }
        }
      }
    }
  }
});


db.createCollection("solutions", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["_id", "student_id", "exercise_id", "file_url"],
      properties: {
        _id: {
          bsonType: "objectId",
          description: "Solution ID must be an ObjectId"
        },
        student_id: {
          bsonType: "objectId",
          description: "Student ID must be a reference to a User ID"
        },
        exercise_id: {
          bsonType: "objectId",
          description: "Exercise ID must be a reference to an Exercise"
        },
        file_url: {
          bsonType: "string",
          pattern: "^(https?:\\/\\/)?[\\da-z.-]+\\.[a-z.]{2,6}([\\/\\w .-]*)*\\/?$",
          description: "File URL must be a valid URL"
        },
        comments: {
          bsonType: "array",
          items: {
            bsonType: "object",
            required: ["commenter_id", "content", "created_at"],
            properties: {
              commenter_id: {
                bsonType: "objectId",
                description: "Commenter ID must be a reference to a User ID"
              },
              content: {
                bsonType: "string",
                description: "Content must be a string"
              },
              created_at: {
                bsonType: "date",
                description: "Created at must be a date"
              }
            }
          }
        },
        grade: {
          bsonType: "object",
          required: ["value", "added_at", "added_by"],
          properties: {
            value: {
              bsonType: "double",
              minimum: 0,
              maximum: 10,
              description: "Grade value must be a number between 0 and 10"
            },
            added_at: {
              bsonType: "date",
              description: "Added at must be a date"
            },
            added_by: {
              bsonType: "objectId",
              description: "Added by must be a reference to a User ID"
            }
          }
        }
      }
    }
  }
});
