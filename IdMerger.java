package com.oracle.interview;

import java.lang.reflect.Array;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class IdMerger {

    public static class IdValue {
        private String system;
        private String systemId;

        public IdValue(String system, String systemId) {
            this.system = system;
            this.systemId = systemId;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            IdValue idValue = (IdValue) o;
            return system.equals(idValue.system) &&
                    systemId.equals(idValue.systemId);
        }

        @Override
        public int hashCode() {
            return Objects.hash(system, systemId);
        }

        public String getSystem() {
            return system;
        }

        public String getSystemId() {
            return systemId;
        }
    }

    public static class IdCollection {

        private final String grpId;
        private final Set<IdValue> ids;

        public IdCollection(String grpId) {
            this(grpId, new HashSet<>());
        }

        public IdCollection(String grpId, Set<IdValue> ids) {
            this.grpId = grpId;
            this.ids = ids;
        }

        public void addId(IdValue id) {
            ids.add(id);
        }

        public String getGrpId() {
            return grpId;
        }

        public Set<IdValue> getIds() {
            return ids;
        }
    }

    public static class IdEntry {

        private String grpId;
        private IdValue idValue;

        public IdEntry(String grpId, IdValue idValue) {
            this.grpId = grpId;
            this.idValue = idValue;
        }

        public IdEntry(String grpId, String system, String systemId) {
            this.grpId = grpId;
            this.idValue = new IdValue(system, systemId);
        }

        public String getGrpId() {
            return grpId;
        }

        public IdValue getIdValue() {
            return idValue;
        }

        public String getSystem() {
            return idValue.getSystem();
        }

        public String getSystemId() {
            return idValue.getSystemId();
        }

        @Override
        public String toString() {
            return "IdEntry{" +
                    "grpId='" + grpId + '\'' +
                    ", system='" + getSystem() + '\'' +
                    ", systemId='" + getSystemId() + '\'' +
                    '}';
        }
    }

    public static class IdGenerator {
        private long _nextId = 0;
        public String getNextId() {
            _nextId += 1;
            return String.valueOf(_nextId);
        }
    }

    private final IdGenerator idGen = new IdGenerator();

    public List<IdEntry> merge(List<IdEntry> leftItems, List<IdEntry> rightItems, boolean replaceLeftIds) {
        List<IdCollection> idCollectionListLeft = groupByGrpId(leftItems, replaceLeftIds);
        List<IdCollection> idCollectionListRight = groupByGrpId(rightItems, false);

        Map<IdValue, IdCollection> idValueToCollection = new HashMap<>();
        List<IdCollection> unMatchedFromRight = new ArrayList<>();

        idCollectionListLeft.forEach(idCollection -> {
            idCollection.getIds().forEach(id -> idValueToCollection.put(id, idCollection));
        });

        idCollectionListRight.forEach(idCollection -> {
            Optional<IdCollection> match = idCollection.getIds().stream().map(idValueToCollection::get).filter(Objects::nonNull).findAny();
            if (match.isPresent()) {
                IdCollection matchedCollection = match.get();
                idCollection.getIds().forEach(matchedCollection::addId);
            } else {
                unMatchedFromRight.add(new IdCollection(idGen.getNextId(), idCollection.getIds()));
            }
        });

        Set<String> grpIds = new HashSet<>();
        List<IdCollection> matchedFromLeftJoin = new ArrayList<>();
        idValueToCollection.values().forEach(idCol -> {
            if (! grpIds.contains(idCol.getGrpId())) {
                matchedFromLeftJoin.add(idCol);
                grpIds.add(idCol.getGrpId());
            }
        });

        List<IdEntry> merged = new ArrayList<>();
        Stream.concat(matchedFromLeftJoin.stream(), unMatchedFromRight.stream()).forEachOrdered(idCollection -> {
            idCollection.getIds().forEach(idValue -> merged.add(new IdEntry(idCollection.getGrpId(), idValue)));
        });

        return merged;
    }

    private List<IdCollection> groupByGrpId(List<IdEntry> items, boolean replaceId) {
        Map<String, List<IdEntry>> map = items.stream().collect(Collectors.groupingBy(IdEntry::getGrpId, Collectors.toList()));
        return map.entrySet().stream().map(e -> {
            String grpId = e.getKey();
            List<IdEntry> ids = e.getValue();
            IdCollection idCollection = replaceId ? new IdCollection(idGen.getNextId()) : new IdCollection(grpId);
            ids.forEach(id -> idCollection.addId(id.getIdValue()));
            return idCollection;
        }).collect(Collectors.toList());
    }

    public static void main(String[] args) {
        List<IdEntry> i1 = Arrays.asList(
                new IdEntry("a", "PAN", "PAN-1"),
                new IdEntry("b", "PAN", "PAN-2"),
                new IdEntry("b", "DL", "DL-2"),
                new IdEntry("c", "PAN", "PAN-3")
        );

        List<IdEntry> i2 = Arrays.asList(
                new IdEntry("a", "PAN", "PAN-3"),
                new IdEntry("a", "VID", "VID-3"),
                new IdEntry("b", "DL", "DL-1"),
                new IdEntry("b", "PAN", "PAN-1"),
                new IdEntry("c", "PAN", "PAN-4"),
                new IdEntry("c", "VID", "VID-4")
        );

        List<IdEntry> i3 = Arrays.asList(
                new IdEntry("a", "AADH", "AADH-4"),
                new IdEntry("a", "VID", "VID-4"),
                new IdEntry("a", "ORCL", "ORCL-4"),
                new IdEntry("x", "DL", "DL-1"),
                new IdEntry("x", "ORCL", "ORCL-1"),
                new IdEntry("y", "ORCL", "ORCL-2"),
                new IdEntry("y", "DL", "DL-2"),
                new IdEntry("z", "VID", "VID-3"),
                new IdEntry("z", "ORCL", "ORCL-3")
        );

        System.out.println("items1 = ");
        i1.forEach(System.out::println);

        System.out.println("\n\nitems2 = ");
        i2.forEach(System.out::println);

        System.out.println("\n\nitems3 = ");
        i3.forEach(System.out::println);

        IdMerger merger = new IdMerger();

        List<IdEntry> merged = merger.merge(
                merger.merge(i1, i2, true),
                i3,
                false
        );

        System.out.println("\n\nmerged items ((i1 + i2) + i3) = ");
        merged.forEach(System.out::println);
    }

}
