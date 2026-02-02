# Created by haydenjeong at 2026-01-31
Feature: Validate Github API
  # Enter feature description here

  Scenario: Github getrepo API checks
    Given I have github auth credentials
    When I hit getrepo API
    Then I get status code 200
    # Enter steps here