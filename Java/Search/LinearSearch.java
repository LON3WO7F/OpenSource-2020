import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

public class LinearSearch {

	private static final int ELEMENT_NOT_FOUND = -1;

	public static void main(String[] args) {
		// Create range of values to use in linear search
		List<Integer> listToSearch = setOfNumbers();
		// return position of value to find
		int elementToFind = 47;
		int index = findNumberWithLinearSearch(listToSearch, elementToFind);
		// Display menssage
		printMessage(elementToFind, index);
		elementToFind = 99;
		index = findNumberWithLinearSearch(listToSearch, elementToFind);
		printMessage(elementToFind, index);
	}

	private static void printMessage(int elementToFind, int index) {
		if (ELEMENT_NOT_FOUND == index) {
			System.out.println("Element " + elementToFind + " not found.");
		} else {
			System.out.println(
					"Element " + elementToFind + " found. Index is: " + index);
		}
	}

	private static int findNumberWithLinearSearch(List<Integer> listToSearch,
			int elementToFind) {
		// create range
		return IntStream.range(0, listToSearch.size())
				// Interact each element on list and compare value is equal the
				// searched
				.filter(element -> listToSearch.get(element)
						.equals(elementToFind))
				// If founded, return the index
				.findFirst()
				// If did not find, return -1
				.orElse(ELEMENT_NOT_FOUND);

	}

	private static List<Integer> setOfNumbers() {
		List<Integer> listToSearch = new ArrayList<>();
		listToSearch.add(13);
		listToSearch.add(22);
		listToSearch.add(3);
		listToSearch.add(443);
		listToSearch.add(51);
		listToSearch.add(236);
		listToSearch.add(47);
		listToSearch.add(8);
		listToSearch.add(95);
		listToSearch.add(10);
		listToSearch.add(18971);
		listToSearch.add(8);
		listToSearch.add(13);
		listToSearch.add(10984);
		listToSearch.add(1235);
		return listToSearch;
	}

}
