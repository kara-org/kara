import 'dart:async';

import 'package:cpf_cnpj_validator/cnpj_validator.dart';
import 'package:cpf_cnpj_validator/cpf_validator.dart';

import 'constants.dart';
import 'functions_util.dart';

mixin Validator {
  static final Pattern emailPattern =
      r'^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$';

  final validateField =
      StreamTransformer<String, String>.fromHandlers(handleData: (field, sink) {
    if (field.isEmpty) {
      sink.addError(DESCRIPTION_MISSING_FIELD);
    } else {
      sink.add(field);
    }
  });

  final validatePhone =
      StreamTransformer<String, String>.fromHandlers(handleData: (phone, sink) {
    if (phone.length == 14 || phone.length == 15) {
      sink.add(phone);
    } else if (phone.isEmpty) {
      sink.addError(DESCRIPTION_MISSING_FIELD);
    } else {
      sink.addError(DESCRIPTION_INVALID_PHONE);
    }
  });

  final validateJustPhone =
      StreamTransformer<String, String>.fromHandlers(handleData: (phone, sink) {
    if (phone.length == 14 || phone.length == 15) {
      sink.add(phone);
    } else {
      sink.addError(DESCRIPTION_INVALID_PHONE);
    }
  });

  final validatePassword =
      StreamTransformer<String, String>.fromHandlers(handleData: (password, sink) {
    if (password.length > 3) {
      sink.add(password);
    } else if (password.isEmpty)
      sink.addError(DESCRIPTION_MISSING_FIELD);
    else {
      sink.addError(DESCRIPTION_INVALID_PASSWORD);
    }
  });

  final validateJustNumero = StreamTransformer<String, String>.fromHandlers(
      handleData: (numero, sink) {
    if (Functions.isNumeric(numero) || numero.isEmpty) {
      sink.add(numero);
    } else {
      sink.addError(DESCRIPTION_INVALID_NUMBER);
    }
  });

  final validateNumero = StreamTransformer<String, String>.fromHandlers(
      handleData: (numero, sink) {
    if (Functions.isNumeric(numero)) {
      sink.add(numero);
    } else {
      sink.addError(DESCRIPTION_INVALID_NUMBER);
    }
  });

  final validateEmail =
      StreamTransformer<String, String>.fromHandlers(handleData: (email, sink) {
    RegExp regExp = RegExp(emailPattern);
    if (regExp.hasMatch(email)) {
      sink.add(email);
    } else if (email.isEmpty) {
      sink.addError(DESCRIPTION_MISSING_FIELD);
    } else {
      sink.addError(DESCRIPTION_INVALID_EMAIL);
    }
  });

  final validateJustEmail =
      StreamTransformer<String, String>.fromHandlers(handleData: (email, sink) {
    RegExp regExp = RegExp(emailPattern);
    if (regExp.hasMatch(email) || email.isEmpty) {
      sink.add(email);
    } else {
      sink.addError(DESCRIPTION_INVALID_EMAIL);
    }
  });

  final validateCPF =
      StreamTransformer<String, String>.fromHandlers(handleData: (cpf, sink) {
    if (CPFValidator.isValid(cpf)) {
      sink.add(cpf);
    } else if (cpf.isEmpty) {
      sink.addError(DESCRIPTION_MISSING_FIELD);
    } else {
      sink.addError(DESCRIPTION_INVALID_CPF);
    }
  });

  final validateCNPJ =
      StreamTransformer<String, String>.fromHandlers(handleData: (cnpj, sink) {
    if (CNPJValidator.isValid(cnpj)) {
      sink.add(cnpj);
    } else if (cnpj.isEmpty) {
      sink.addError(DESCRIPTION_MISSING_FIELD);
    } else {
      sink.addError(DESCRIPTION_INVALID_CNPJ);
    }
  });
}
