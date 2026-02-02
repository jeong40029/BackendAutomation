# Created by haydenjeong at 2026-01-31
Feature: Verify if books are added or deleted by using Library API
  # Enter feature description here
  @library
  Scenario: Verify AddBook API Functionality
    Given Book details that needs to be added to library
    When we execute AddBook Post API method
    Then book is successfully added

    @library
    Scenario Outline: Verify AddBook API Functionality
    Given Book details with <isbn> and <aisle>
    When we execute AddBook Post API method
    Then book is successfully added
      Examples:
      |isbn|aisle|
      |ddge|17473|